/*
    FILE:       smoss.js
    AUTHOR:     mmiddleton
    DATE:       22 FEB. 2018
*/

$('#urlInput').on ('keyup', function (keyPressed){
    // TODO:    Find a way to remove form submission when a user hits the enter key.
    if (keyPressed.which == 13) {
        keyPressed.preventDefault ();
        addURLToList ();
        $('#urlInput').val ('');
        console.log ('enter pressed!');
        return;
    }
});

function addURLToList () {
    $('#urlList').html ($('#urlList').html () + '<div class="row"><div class="eleven columns"><p>' + $('#urlInput').val () + '</p></div><div class="one column"><input type="button" class="delete button" onclick="removeLinkedUrl()" value=" X "></div></div>');
}

function removeLinkedUrl () {
    // TODO: Remove corresponding URL from list!'
    // console.log ('Removed link from URL.');
}
