
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