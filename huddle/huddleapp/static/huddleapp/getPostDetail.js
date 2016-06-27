/*
 * getPostDetail.js
 * get the post detail
 */

function getPostDetail(id){
  console.log("getPostDetail id: " + id);
    $.get("/" + id + "/post/")
      .done(function(json){
        $(".detail-title").text(json["title"]);
        $(".detail-body").text(json["body"]);
        $(".instructor-answer").text(json["instructor_answer"]);
        $(".student-answer").text(json["student_answer"]);
        $(".direct-followups").empty();
        var followups = json["followups"]
        if(followups){
          for(var i = followups.length-1; i >= 0; i--){
            // TODO: Make this more readable
            var element = '<li><div class="bottom-small-spaced"><span class="followup-title">'
                          + followups[i]["author"]
                          + '</span></div><p class="followup-body bottom-small-spaced bottom-separated">'
                          + followups[i]["followup_text"]
                          + '</p>';

            var secondaryList = '<ul class="secondary-followups list-unstyled">';
            var followupComments = followups[i]["followupComments"];
            for(var j = followupComments.length-1; j >= 0; j--){
              secondaryList += '<li class="bottom-separated">'
                              +   '<div class="bottom-small-spaced">'
                              +     '<span class="followup-title">'
                              +       followupComments[j]["author"]
                              +     '</span>'
                              +   '</div>'
                              +   '<p class="followup-body bottom-small-spaced">'
                              +     followupComments[j]["comment_text"]
                              +   '</p>'
                              + '</li>'
            }
            secondaryList += '<li class="bottom-separated">'
                            +   '<input type="text" placeholder=" Add a comment..." class="comment-input commentInput" id="' + followups[i]["id"] + '">'
                            +   '<button type="button" class="btn btn-default btn-xs btn-custom addComment" aria-label="Left Align" id="' + followups[i]["id"] + '">'
                            +     '<span class="glyphicon glyphicon-save"aria-hidden="true"></span> Submit'
                            +   '</button>'
                            +'</li>'
                            +'</ul>'
            console.log(secondaryList);
            element += secondaryList;
            element += '</li>'
            $(".direct-followups").append(element);
          }
        }
        var newFollowup =  '<li>'
                          +  '<div class="bottom-small-spaced top-padding">'
                          +    '<span class="followup-title">Add a followup discussion:</span>'
                          +  '</div>'
                          +  '<div class="top-padding bottom-small-spaced">'
                          +    '<input type="text" placeholder=" Add a followup..." class="comment-input" id="followupInput">'
                          +    '<button type="button" class="btn btn-default btn-sm btn-custom" aria-label="Left Align" id="addFollowup">'
                          +       '<span class="glyphicon glyphicon-comment"aria-hidden="true"></span> Submit'
                          +    '</button>'
                          +  '</div>'
                          +'</li>';
        $(".direct-followups").append(newFollowup);
        addFollowupComment(json["id"]);
        addFollowup(json["id"]);
        $(".detail").show();
      });

}

function addFollowup(id){
  $("#addFollowup").click(function(){
    var input = $("#followupInput").val();
    $.post("/followup/", {body: input, post_id: id})
      .done(function(data){
        getPostDetail(id);
      });
  });
}

function addFollowupComment(id){
  $(".addComment").click(function(){
    console.log(this.id);
    var input = $("#" + this.id + ".commentInput").val();
    $.post("/followupComment/", {followup_id:this.id, body: input})
      .done(function(data){
        getPostDetail(id);
      });
  });
}

function addStudentEdit(){
  $("#addStudentAnswer").click(function(){
    $(".student-answer").toggle();
    $("#studentEdit").toggle();
    $("#submitStudentAnswer").toggle();
    $("#studentEdit").val($(".student-answer").text());
  });
}

function submitEdit(id){
  $("#submitStudentAnswer").click(function(){
    $.post("/studentEdit/", {post_id: id, body: $("#studentEdit").val()})
      .done(function(data){
        getPostDetail(id);
        $("#studentEdit").hide();
        $("#submitStudentAnswer").hide();
        $(".student-answer").show();
      });
  });
  }

function clickPost(){
  $("li.post").click(function(){
    getPostDetail(this.id);
    submitEdit(this.id);
  });
  $(".student-anser").show();
  $("#studentEdit").hide();
  $("#submitStudentAnswer").hide();
  $(".student-answer").show();
  
}


$(".detail").hide();
clickPost();
addStudentEdit();

