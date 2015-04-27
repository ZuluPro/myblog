tinyMCE.init({
	mode: "exact",
	elements: "id_content",
	theme: "advanced",
	skin : "o2k7",
	skin_variant : "silver",
	height: "250",
	width: "800",
	relative_urls: false,
	language: "{{ language }}",
	directionality: "{{ directionality }}",
	spellchecker_languages : "{{ spellchecker_languages }}",
	spellchecker_rpc_url : "{{ spellchecker_rpc_url }}",
	theme_advanced_toolbar_location : "top",
	theme_advanced_toolbar_align : "left",
	theme_advanced_statusbar_location : "bottom",
	theme_advanced_resizing : true,
	plugins: "contextmenu,directionality,fullscreen,paste,preview,searchreplace,spellchecker,visualchars,wordcount,prism",
        toolbar: "prism",
	paste_auto_cleanup_on_paste : true,
	theme_advanced_buttons1 : "formatselect,fontsizeselect,|,pastetext,pasteword,|,search,replace,|,visualchars,visualaid,cleanup,code,preview,fullscreen", //,spellchecker",
	theme_advanced_buttons2 : "prism,|,bold,italic,underline,strikethrough,|,forecolor,backcolor,removeformat,|,justifyleft,justifycenter,justifyright,justifyfull,|,sub,sup,|,bullist,numlist,|,outdent,indent,|,link,unlink,anchor,image,blockquote,hr,charmap",
	file_browser_callback : "mce_filebrowser",
	external_link_list_url : "{% url 'tinymce-external-links' %}",
	external_image_list_url : "{% url 'tinymce-external-images' %}",
	external_media_list_url : "{% url 'tinymce-external-files' %}",
        theme_advanced_blockformats : "p,div,code,h3,h4,h5,h6,blockquote",
        setup : function(editor) {
            editor.onInit.add(function (editor) {
                tinymce.ScriptLoader.load('/static/prism/prism.js');
                tinymce.activeEditor.dom.loadCSS('/static/prism/themes/prism.css');
            });
        }
});
