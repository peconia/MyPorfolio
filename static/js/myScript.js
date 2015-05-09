jQuery(window).load(function () {
 
 
    var $container = jQuery('#art-images');
     
    $container.masonry({
    itemSelector: '.image-box',
    columnWidth: '.image-box'
    });

 
}); 
