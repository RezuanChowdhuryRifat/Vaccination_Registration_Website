function covidcheck(){
    let checker = document.getElementById("checkcovid").value

   if(checker == 2){
     window.location.replace("/registration")
   } 
   else{
   document.getElementById("message").innerText = "You are not eligible right now"
     
   }
 }

 function showOTP(){
   let getId = document.getElementById('otp')
   getId.style.display ="block"
 }