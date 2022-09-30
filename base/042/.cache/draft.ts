import {evaluate, write, puts} from "./shell";

class Car{
    private pass: number; // Passageiros
    private passMax: number; // limite de Passageiros
    private gas: number; // tanque
    private gasMax: number; // limite do tanque
    private km: number; // quantidade de quilometragem

    constructor() { //todo
    }

    public setPass(pass: number): void { //todo
    }
    
    public setGas(gas: number): void { //todo
    }

    public setKm(km: number): void { //todo
    }

    public getGas(): number { //todo
    }
    public getKm(): number { //todo
    }
    public getPass(): number { //todo
    }

    public enter() {
        this.setPass(this.pass + 1);
    }

    public leave() {
        this.setPass(this.pass - 1);  
    }

    public fuel(gas: number) {
        this.setGas(this.gas + gas);
    }

    public drive (km: number) {
        if(this.pass == 0) {
            puts("fail: nao ha ninguem no carro");
        } else if(this.gas == 0) {
            puts("fail: tanque vazio");
        }
        else if(this.gas < km) {
            puts("fail: tanque vazio apos andar " + this.gas + " km");
            this.setKm(this.km + this.gas);
            this.gas = 0;
        } else{
            this.gas = this.gas - km;
            this.km = this.km + km;
        }
    }    

    public toString() {
        return "pass: " + this.pass + ", gas: " + this.gas + ", km: " + this.km;
    }
};


function main() {
    let chain = new Map();
    let param = [];
    let car = new Car();

    chain.set("enter",      () => car.enter());
    chain.set("leave",      () => car.leave());
    chain.set("show",       () => puts(car.toString()));
    chain.set("drive",      () => car.drive(+param[1]));
    chain.set("fuel",       () => car.fuel(+param[1]));
    chain.set("help",       () => puts("show, enter, leave, drive, fuel, help, end"));

    evaluate(chain, param);
}

main()
