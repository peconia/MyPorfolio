// Load is used to ensure all images have been loaded, impossible with document
 
jQuery(window).load(function () {
 
 
    var $container = jQuery('#art-images');
     
     
     
    // Creates an instance of Masonry on #posts
     
    $container.masonry({
    itemSelector: '.image-box',
    columnWidth: '.image-box'
    });

 
}); 
