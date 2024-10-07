function escapeHTML(str) {
    return str.replace(/[&<>"']/g, function(match) {
      const escape = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      };
      return escape[match];
    });
  }
  
  const userInput = "<script>alert('XSS')</script>";
  const escapedInput = escapeHTML(userInput);
  console.log(escapedInput); // Output: &lt;script&gt;alert('XSS')&lt;/script&gt;
  