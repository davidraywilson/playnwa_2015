/**
 * @license Copyright (c) 2003-2014, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here.
	// For complete reference see:
	// http://docs.ckeditor.com/#!/api/CKEDITOR.config

	// The toolbar groups arrangement, optimized for two toolbar rows.
	config.toolbarGroups = [
		{ name: 'clipboard',   groups: [ 'clipboard', 'undo' ] },
		{ name: 'editing',     groups: [ 'find', 'selection', 'spellchecker' ] },
		{ name: 'links' },
		{ name: 'insert' },
		{ name: 'forms' },
		{ name: 'tools' },
		{ name: 'document',	   groups: [ 'mode', 'document', 'doctools' ] },
		{ name: 'others' },
		'/',
		{ name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ] },
		{ name: 'paragraph',   groups: [ 'list', 'indent', 'blocks', 'align', 'bidi' ] },
		{ name: 'styles' },
		{ name: 'colors' },
		{ name: 'about' }
	];

	// Remove some buttons provided by the standard plugins, which are
	// not needed in the Standard(s) toolbar.

	// Set the most common block elements.
	config.format_tags = 'p;h1;h2;h3;h4;h5;pre';

	// Simplify the dialog windows.
	config.removeDialogTabs = 'image:advanced;link:advanced';

	config.extraPlugins = 'justify';

    config.allowedContent = true;

    config.stylesSet = [
		{ name: 'float left', element: 'p', attributes: {'class': 'left'} },
        { name: 'info button', element: 'a', attributes: {'class': 'btn info'} },
		{ name: 'action button', element: 'a', attributes: {'class': 'btn action'} },
		{ name: 'info hollow button', element: 'a', attributes: {'class': 'hollow-btn info'} },
		{ name: 'action hollow button', element: 'a', attributes: {'class': 'hollow-btn action'} },
        { name: 'large p', element: 'p', attributes: {'class': 'large'} },
		{ name: 'large p info', element: 'p', attributes: {'class': 'large info'} },
		{ name: 'large p action', element: 'p', attributes: {'class': 'large action'} },
		{ name: 'page-title', element: 'p', attributes: {'class': 'page-title'} },
    ];
};
