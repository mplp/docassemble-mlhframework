/** Put this in your branding package/org framework. */
$(document).on('daPageLoad', async function() {
  /**
   * Add a script to the page only when an appropriate. In this case, the script will
   *     add a Survey Monkey iframe. You can abstract this more using window-level
   *     variables.
   * 
   * Avoid layout shift by using an initial dummy element of the same size as the
   * final element plus some other details: https://web.dev/articles/optimize-cls
   * Web archive: https://web.archive.org/web/20260428160404/https://web.dev/articles/optimize-cls
   */

  const relocated_class = `relocated`;
  const $script_parent = $(`#survey_monkey1`);

  // Stops executing this code when 1. a specific element missing or
  // 2. we have already done this.
  if ( !$script_parent[0] || $script_parent.hasClass( relocated_class ) ) {
    return;
  }

  // Add the script to the page
  $script_parent.append( $survey_monkey_script );

  // Storing the state of affairs on the page
  $script_parent.addClass( relocated_class );
  
});