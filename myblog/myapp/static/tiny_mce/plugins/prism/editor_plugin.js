/**
 * Prism plugin by Metrakit
 * contact@jordane.net
*/
(function() {
tinymce.create('tinymce.plugins.PrismPlugin', {
    init : function(ed, url) {
        ed.onNodeChange.add(function(ed, cm, n) {
            cm.setActive('prism', n.nodeName == 'IMG');
        });
        ed.addButton('prism', {
            icon: "code",
            onclick: function() {
                ed.windowManager.open({
                    title: 'Insert your code',
                    width: 700,
                    height: 400,                
                    url: '/zinnia_tinymce/prism-form.html',
                });
            }
        });
    },
    createControl : function(n, cm) {
        return null;
    },
    getInfo : function() {
        return {
            longname : 'Prism plugin',
            author : 'Some author',
            authorurl : 'http://tinymce.moxiecode.com',
            infourl : 'http://wiki.moxiecode.com/index.php/TinyMCE:Plugins/prism',
            version : "1.0"
        };
    }
});
tinymce.PluginManager.add('prism', tinymce.plugins.PrismPlugin);

$('body').on('submit', "#prism-form", function (e) {
    var editor = tinymce.activeEditor;
    var language = $('[name="language"]').val();
    var code = $('[name="code"]').val();
    var line_numbers = $('[name="line-numbers"]').val();
    var text = '<pre class="language-' + language;
    if (line_numbers) text += " line-numbers"
    text += '"><code>' + code + '</code></pre>';
    editor.execCommand('mceInsertContent', false, text);
    tinyMCEPopup.close(); 
});
})();

