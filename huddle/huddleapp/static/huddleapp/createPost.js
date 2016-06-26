/* 
 * createPost.js
 * Create a post
 */

function addPost(){
  $("#addPost").click(function() {
    // get the values from the fields
    var title = $("#addTitle").val();
    var body = $("#addBody").val();
    $.post("/post/", {title: title, body: body})
      .done(function(data){
        getPosts();
      });
  });
}

addPost();

