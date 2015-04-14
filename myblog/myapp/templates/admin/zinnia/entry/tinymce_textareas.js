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
	plugins: "contextmenu,directionality,fullscreen,paste,preview,searchreplace,spellchecker,visualchars,wordcount",
	paste_auto_cleanup_on_paste : true,
	theme_advanced_buttons1 : "formatselect,fontsizeselect,|,undo,redo,|,cut,copy,paste,pastetext,pasteword,|,search,replace,|,visualchars,visualaid,cleanup,code,preview,fullscreen",
	theme_advanced_buttons2 : "bold,italic,underline,strikethrough,|,forecolor,backcolor,removeformat,|,justifyleft,justifycenter,justifyright,justifyfull,|,sub,sup,|,bullist,numlist,|,outdent,indent,|,link,unlink,anchor,image,blockquote,hr,charmap,",
	theme_advanced_buttons3 : "",
	file_browser_callback : "mce_filebrowser",
	external_link_list_url : "{% url 'tinymce-external-links' %}",
	external_image_list_url : "{% url 'tinymce-external-images' %}",
	external_media_list_url : "{% url 'tinymce-external-files' %}",
        theme_advanced_blockformats : "p,div,h1,h2,h3,h4,h5,h6,blockquote,dt,dd,code,samp,pre"
});
