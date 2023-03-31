
const backgroundimg = document.querySelector("#backgroundimg");
const musicloading = document.getElementById("musicloading");
const closemusic = document.getElementById("closemusic");
const listenmusiconly = document.getElementById("listenmusiconly");
const watchvideo = document.getElementById("watchvideo");
const audioloadingwithcontent = document.getElementById('audioloadingwithcontent');
const musicytvideo =  document.getElementById("musicytvideo");
const content = document.getElementById('inputtedtext');
const start_stop_voice = document.getElementById('startrecord');
const chatbox =  document.getElementById("chatbox");
const button = document.getElementById('startstopimg');
const elem = document.querySelector("#loadingborder");




(function(){
    document.addEventListener("mousemove", background);
    function background(e){

        let w = window.innerWidth/2;
        let h = window.innerHeight/2;
        let mouseX = e.clientX;
        let mouseY = e.clientY;
        let x = 50-(mouseX-w)*0.03;
        let y = 50-(mouseY-h)*0.03;
        backgroundimg.style.transform = 'translate('+x+'px,'+y+'px)';
    
    }

})();


function openPlayer(values){
    // let values =  $(this).closest('span').values;
    elem.className = 'loadanimationsquare';
    musicloading.style.display = "none";
    closemusic.style.display = "block";
    listenmusiconly.style.display = "block";
    watchvideo.style.display = "none";
    audioloadingwithcontent.style.display = 'none';
    musicytvideo.style.display = "block";
    // $(this).closest('a').href = "https://www.youtube.com/embed/"+values;
    if(musicytvideo.src != 'https://www.youtube.com/embed/'+values+'?autoplay=1'){
        musicytvideo.src = 'https://www.youtube.com/embed/'+values+'?autoplay=1';
    }   
}

function closePlayer(){
    elem.className = 'load';
    closemusic.style.display = "none";
    listenmusiconly.style.display = "none";
    watchvideo.style.display = "none";
    musicytvideo.style.display = "none";
    musicytvideo.src = '';
    audioloadingwithcontent.style.display = 'none';
    musicloading.style.display = 'none';
}


function musicPlayer(){
    elem.className = 'loadinganimationrotate';
    audioloadingwithcontent.style.display = 'flex';
    musicloading.style.display = 'none';
    closemusic.style.display = "block";
    listenmusiconly.style.display = "none";
    watchvideo.style.display = "block";
    musicytvideo.style.display = "none";
}
function watchPlayer(){
    elem.className = 'loadanimationsquare';
    musicloading.style.display = "none";
    closemusic.style.display = "block";
    listenmusiconly.style.display = "block";
    watchvideo.style.display = "none";
    audioloadingwithcontent.style.display = 'none';
    musicloading.style.display = 'none';
    musicytvideo.style.display = "block";
}


function scrollToLatest(){
   chatbox.scrollTo({left: 0, behavior: 'smooth' });
}





window.onload = () => {
    start_stop_voice.addEventListener('click', () => {
      if (button.className === 'stopimg') {
        document.querySelector("#loadingborder").className = 'load';
        closemusic.style.display = "none";
        listenmusiconly.style.display = "none";
        watchvideo.style.display = "none";
        musicytvideo.src = '';
        audioloadingwithcontent.style.display = 'none';
        musicloading.style.display = 'none';
        start_stop_voice.style.background = 'linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0))';


        $.ajax({
          type: "POST",
          url:"voicerecord",
          data: {"ques": content.value},
          dataType:'json',
          // success: function(sys){

          //   $(body).replaceWith(sys)
          // }
        });

        
        console.log(content.value);

        content.value = "";
        recognition.stop();
        button.className = 'startimg';
      } else {


        musicloading.style.display = "flex";
            elem.style.borderRadius = "5px";
            elem.className = 'loadinganimationrotate';
            closemusic.style.display = "none";
            listenmusiconly.style.display = "none";
            watchvideo.style.display = "none";
            musicytvideo.style.display = "none";
            musicytvideo.src = '';
            audioloadingwithcontent.style.display = 'none';
            start_stop_voice.style.background = 'linear-gradient(135deg, rgba(252, 7, 7, 0.589), rgba(11, 23, 194, 0.24))';
            button.className = "stopimg";

            recognition.start();
      }
    });


    const recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.onresult = function (event) {
      let result = '';
      for (let i = event.resultIndex; i < event.results.length; i++) {
        result += event.results[i][0].transcript;
      }
      content.value = result;
    };
    content.value = "";
  };

  function senddata(){
    const cont = document.getElementById("inputtedtext").value;
    $.ajax({
      type: "POST",
      url:"voicerecord",
      data: {"ques": cont},
      dataType:'json',
    });
    cont = none;
  }
