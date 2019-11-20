// function show_window(){
    //     // window.open('/facebook-form','_blank','width=700,height=500')
    //     $.ajax({
    //       type: 'POST',
    //       url: '/ajax',
    //       success: function(result){
    //         console.log(result)
    //         setTimeout(window.open(result.url,'_blank','width=700,height=500'),5000)
    //         window.close()
    //       },
    //       async:false
    //     });
    // }


// window.location.href = "/facebook";
//$('#ex1').load("./facebook-form")
//<!--setTimeout(function(){$("#ex1").modal({escapeClose: false,clickClose: false,showClose: false})},5000)-->


//Main
var start_time;
var stop_time;

//create youtube frame
var current_url = 'http://youtube.com?v=u3A7bmEOtaU'; // id of link youtube
var video; //Api object
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementById("youtube-tracking-script");
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

//create video
function onYouTubeIframeAPIReady() {
    video = new YT.Player('video-youtube', {
        height: '352',
        width: '100%',
        videoId: getIdFromUrlYtb(current_url),
        playerVars: {rel: 0, showinfo: 0},
        events: {
            'onStateChange': videoPlay
        }
    });
}

function videoPlay(event) {
    if (event.data == YT.PlayerState.PLAYING) {
        console.log("YouTube Video is PLAYING!!");
    }
     if (event.data == YT.PlayerState.PAUSED) {
        console.log("YouTube Video is PAUSED!!");
    }
    if (event.data == YT.PlayerState.ENDED) {
        console.log("YouTube Video is ENDING!!");
    }
}

function getIdFromUrlYtb(url){
    return url.split('v=')[1]
}

//change url btn click
function changeYoutubeUrl(){
    current_url = $("#ytb_link").val()
    var videoId = getIdFromUrlYtb(current_url)
    video.loadVideoById(videoId)
}

function startTimeClick(element){
    $(element).attr("disabled",true);
    start_time = video.getCurrentTime();
    console.log(start_time)
}

function stopTimeClick(element){
    $(element).attr("disabled",true);
    stop_time = video.getCurrentTime();
    console.log(stop_time)
    $.ajax({
        data:{
            'url':current_url,
            'start_time':start_time,
            'stop_time':stop_time
        },
        type:'POST',
        url:'/cut_video'
    })
    .done(function(data){
        console.log(data.output)
    })
}