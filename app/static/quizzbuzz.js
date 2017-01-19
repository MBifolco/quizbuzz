function GetQuizzes(){
    return $.get( "../quizzes/" );
}
function AddQuiz(){
    var name = $('#')
}
function UpdateQuizlist(){
    var quizzes;
    $('#quizzes').html("")
    GetQuizzes().done(function(data) { 
        quizzes = data; 
        for (quiz in quizzes) {
            $('#quizzes').append("<div>" + quizzes[quiz].name + "</div>")
        } 
    });  
}
function FormatSerializedData(data){
    var obj = {}
    data.each(function(){
        var name = $(this).attr('name');
        var value = $(this).val();
        console.log(name + " " +value)
        obj[name] = value
    });
    return JSON.stringify(obj);
}

$( document ).ready(function() {
    UpdateQuizlist()
    $('#quiz_add').click(function(){
        json = FormatSerializedData($(".add_quiz")); 
        $.ajax({
            type: 'POST',
            url: '../quizzes/',
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            data: json,
            success:function(data) {
              UpdateQuizlist(data); 
            }
        });
        console.log(json)
    });
});