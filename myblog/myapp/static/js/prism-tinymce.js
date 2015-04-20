/**
 * Prism plugin by Metrakit
 * contact@jordane.net
*/
var languageList = [
    'Markup', 'CSS', 'Javascript', 'PHP', 'Sass', 'Bash',
    'SQL', 'HTTP', 'Ruby', 'Ini', 'Apache', 'Git', 'Less',
    'Markdown'
];
var menuLanguages = [];
tinymce.each(languageList, function(language) {
    menuLanguages.push({
        text: language,
        value: language.toLowerCase()
    });
});
tinymce.create('tinymce.plugins.prismPlugin', {
    init : function(ed, url) {
        ed.addCommand('mcePrism', function() {
            ed.windowManager.open({
                file : url + '/dialog.htm',
                width : 320 + ed.getLang('prism.delta_width', 0),
                height : 120 + ed.getLang('prism.delta_height', 0),
                inline : 1
            }, {
                plugin_url : url, // Plugin absolute URL
                some_custom_arg : 'custom arg'
            });
            ed.addButton('prism', {
                title : 'prism.desc',
                cmd : 'mcePrism',
                image : url + '/img/prism.gif
            });
            ed.onNodeChange.add(function(ed, cm, n) {
                cm.setActive('prism', n.nodeName == 'IMG');
            });
            ed.addButton('prism', {
                icon: "code",
                onclick: function() {

                    editor.windowManager.open({
                        title: 'Insert your code',
                        width: 600,
                        height: 400,                
                        body: [
                            {
                                type: 'TextBox', 
                                name: 'code', 
                                label: 'Code :',
                                multiline: true,
                                minHeight: 300
                                //rows: 10
                            },
                            {
                                type: 'listbox',
                                name: 'language',
                                label: 'Language :',
                                values: menuLanguages
                              }
                        ],
                        onsubmit: function(e) {
                            editor.insertContent('<pre class="language-' + e.data.language + '"><code>' + e.data.code + '</code></pre>');
                        }
                    });
                }
            });
        });
    },
    createControl : function(n, cm) {
        return null;
    },
    getInfo : function() {
        return {
            longname : 'Prism plugin',
            author : 'Anthony MONTHE',
            authorurl : 'http://tinymce.moxiecode.com',
            infourl : 'http://wiki.moxiecode.com/index.php/TinyMCE:Plugins/prism',
            version : "1.0"
        };
    }
});
tinymce.PluginManager.add('prism', tinymce.plugins.PrismPlugin);
