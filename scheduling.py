const process = (name, status) => {
    return{
        name: name,
        status: status
    }
}

let processes = [process('P0',false),process('P1',false),process('P2',false)];

while (process.length > 0 ){
    for(let i = 0; i < process.length; i++){
        let process = processes[i];
        if(process.status){
            console.log(`${process.name} done! `);
            process = processes.filter(element => element.name !== process.name);

        }
        else{
            process.status = true;
            console.log(`${process.name} is running`);
        }
    }
}
