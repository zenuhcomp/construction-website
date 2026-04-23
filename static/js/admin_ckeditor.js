window.onload = function() {
    var textareas = [
        'id_full_description', 
        'id_description', 
        'id_content'
    ];
    textareas.forEach(function(id) {
        if (document.getElementById(id)) {
            CKEDITOR.replace(id, {
                height: 400,
                allowedContent: true, // Allow all HTML formatting
                extraPlugins: 'image2',
            });
        }
    });
};
