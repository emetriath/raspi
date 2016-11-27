
function initialize_webiopi(){
    webiopi().refreshGPIO(false);
}

function setWheel(mode,speed){
    console.log(mode);
    webiopi().callMacro("setWheel", [mode, speed]);
}

function setTurret(angle){
    console.log(angle);
    webiopi().callMacro("setTurret", [angle]);
}

function gunfire(num){
    console.log(num);
    webiopi().callMacro("gunfire", [num]);
}

function startCamera(){
    webiopi().callMacro("startCamera", [], geCamImage);
}

function geCamImage(macro, args, data){
    
    webiopi().callMacro("geCamImage", [], refreshImage);
}
function refreshImage(macro, args, data){
    document.getElementById("capture").innerHTML = data;
    geCamImage();
}