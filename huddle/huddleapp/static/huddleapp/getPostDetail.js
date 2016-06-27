/*
 * getPostDetail.js
 * get the post detail
 */

function getPostDetail(){
  $("li.post").click(function(){
    console.log("HELLO");
    $.get("/" + this.id + "/post/")
      .done(function(data){
        var json = JSON.parse(data);
        $(".detail-title").text(json[0]["fields"]["title"]);
        $(".detail-body").text(json[0]["fields"]["body"]);
        $(".instructor-answer").text(json[0]["fields"]["instructor_answer"]);
        $(".student-answer").text(json[0]["fields"]["student_answer"]);
      });
  });
}

getPostDetail();
