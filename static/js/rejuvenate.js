"use strict";


// select the comment form, add an event handler for onsubmit that will preventdefault
// make an ajax request(url to route, data you want to send, the callbackfunction(a post ajax request))
// use javascript to manually grab the comment out of the form, which is the data you want to send in the ajax request
// the callback receives a response from the server, hopefully, it is the success message that we returned in server;
// use jquery to append final comment in html (second part of callback)
// console.log to make sure we get success message

function submitComment(evt) {
    evt.preventDefault();

    const comment = $('#comment')

    $.post('/community', comment, (response) => {
        $('ul').append(`<li>${response.global_comment}</li>`);
    } )
    console.log('posted')
}

$('textarea').on('submit', submitComment);