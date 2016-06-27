/* 
 * hideAdd.js
 * hide and show the post details
 */

$("#hidePost").click(function(){
  $(".hide-add").toggle();
  $("#addTitle").val("");
  $("#addBody").val("");
});
