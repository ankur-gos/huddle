/*
 * getPosts.js
 * get and display posts
 */

function getPosts(){
  $.get("/posts/")
    .done(function (data){
      $("#postList").empty();
      var json = JSON.parse(data);
      for(var i = 0; i < json.length; i++){
        var element = '<li class="post" id='
                      + json[i]["pk"]
                      + '><span class="post-title">'
                      + json[i]["fields"]["title"] 
                      + '</span><br><span class="post-text">' 
                      + json[i]["fields"]["body"]
                      + '</span></li>';
        $("#postList").append(element);
      }
    });
}
getPosts();
