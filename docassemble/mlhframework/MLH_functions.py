def strip_end_punctuation(text, punctuation_marks=None):
    """Removes any punctuation marks from the end of the text."""
    if text is None or not isinstance(text, str):
        return text
        
    if punctuation_marks is None:
        punctuation_marks = ['.', ',', '?', '!', ':', ';']
    
    if not isinstance(punctuation_marks, list):
        punctuation_marks = list(punctuation_marks)
    
    text = text.rstrip()
    
    while text and any(text.endswith(mark) for mark in punctuation_marks):
        for mark in punctuation_marks:
            if text.endswith(mark):
                text = text[:-len(mark)]
                text = text.rstrip()
                break
                
    return text
###########################
# temporarily replacing this code to stop filtering urls
from typing import Dict, Optional, List, Union, Any
def make_github_issue(
    repo_owner: str,
    repo_name: str,
    template=None,
    title: Optional[str] = None,
    body: Optional[str] = None,
    label: Optional[str] = None,
) -> Optional[str]:
    """
    Create a new GitHub issue and return the URL.

    Args:
        template: a docassemble template that overrides `title` and `body`
        title: the title for the GitHub issue
        body: the body of the GitHub issue
        label: optional label to add *if* we can verify or create it

    At least one of template, title, and body is required.

    Returns:
        str, the URL for the label if it exists, or None if the issue could not be created
    """
    make_issue_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"

    # Abort early if the configuration or repo owner is invalid
    if not valid_github_issue_config():
        log(
            "Error creating issue: No valid GitHub token provided. "
            "See https://github.com/SuffolkLITLab/docassemble-GithubFeedbackForm#getting-started"
        )
        return None
    if repo_owner.lower() not in _get_allowed_repo_owners():
        log(
            f"Error creating issue: repositories owned by {repo_owner} are not permitted. "
            "See https://github.com/SuffolkLITLab/docassemble-GithubFeedbackForm#getting-started"
        )
        return None

    headers = {
        "Authorization": f"token {_get_token()}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Abort early for private repos
    repo_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    repo_resp = requests.get(repo_url, headers=headers)

    if repo_resp.status_code != 200:
        log(
            f"Cannot access repo {repo_owner}/{repo_name}: "
            f"{repo_resp.status_code} {repo_resp.text}. Maybe it is a private repo?"
            "Check that the PAT has the correct scopes and that the user can write to the repo."
        )
        return None

    # ------------------------------------------------------------------
    # 1. Figure out whether we can safely apply the label
    # ------------------------------------------------------------------
    apply_label = False  # only set to True when we're sure it exists

    if label:
        make_labels_url = (
            f"https://api.github.com/repos/{repo_owner}/{repo_name}/labels"
        )
        get_labels_url = f"{make_labels_url}/{label}"
        has_label_resp = requests.get(get_labels_url, headers=headers)

        if has_label_resp.status_code == 200:
            # Label already exists in the repo
            apply_label = True

        elif has_label_resp.status_code == 404:
            # Try to create the label; this may fail if the token lacks permission
            label_data = {
                "name": label,
                "description": "Feedback from a Docassemble Interview",
                "color": "002E60",
            }
            make_label_resp = requests.post(
                make_labels_url,
                data=json.dumps(label_data),
                headers=headers,
            )
            if make_label_resp.status_code == 201:
                log(
                    f"Created the '{label}' label for the "
                    f"{repo_owner}/{repo_name} repository"
                )
                apply_label = True
            else:
                log(
                    f"Could not create label '{label}': {make_label_resp.status_code} "
                    f"{make_label_resp.text}"
                )
        else:
            # 403, 422, etc. → most likely a permissions issue; skip using the label
            log(
                f"Unable to verify label '{label}': {has_label_resp.status_code} "
                f"{has_label_resp.text}"
            )

    # ------------------------------------------------------------------
    # 2. Derive title/body from a template, if supplied
    # ------------------------------------------------------------------
    if template:
        if hasattr(template, "subject"):
            title = template.subject
        if hasattr(template, "content"):
            body = template.content

    if not title and not body:
        return None

    if not body:
        body = ""

    if not title:
        title = "User feedback"

    # Reject obvious spam before calling GitHub
    if is_likely_spam(body, filter_urls=False):
        log("Error creating issue: the body of the issue was classified as spam")
        return None

    # ------------------------------------------------------------------
    # 3. Assemble and POST the issue
    # ------------------------------------------------------------------
    data: Dict[str, Union[str, List[str]]] = {
        "title": title,
        "body": body,
    }
    if apply_label and label is not None:
        data["labels"] = [label]

    response = requests.post(make_issue_url, data=json.dumps(data), headers=headers)

    if response.status_code == 201:
        return response.json().get("html_url")
    else:
        log(f'Could not create issue "{title}": {response.status_code} {response.text}')
        return None