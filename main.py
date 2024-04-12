from simulator.device_manager import DeviceManager
import argparse
import signal
import sys
import time

def signal_handler(sig, frame, device_manager):
    device_manager.stop_all_devices()
    print("All threads shutdown gracefully...")
    sys.exit(0)
    

def main():
      
    parser = argparse.ArgumentParser(description="parse user options")
    parser.add_argument("--device-type",metavar="-D", type=str,default="DEFAULT",help="Define o tipo de sensor que queremos simular opções:DEFAULT, TEMPERATURE_V1, TEMPERATURE_V2, TEMPERATURE_V3, AIRQUALITY_V1, AIRQUALITY_V2, AIRQUALITY_V3, ENERGY_V1, WATER_V1, GAS_V1, SMARTBUTTON_V1")
    parser.add_argument("--time-interval", metavar="-T",type=int,default=20,help="Intervalo de tempo (em minutos) em que queremos enviar uma mensagem")
    parser.add_argument("--multi",type=str,default=False,help="Simular lista de sensores ao mesmo tempo, o campo time-interval será aplicado equalitativamente a todos os sensores EX: --multi=['ENERGIA','AGUA']")    
    parser.add_argument("--n_instances",type=int,default=1,help="Número de instâncias de cada sensor a ser gerado, ou seja se temos a opção multi com 2 sensores e n_instances = 2 então numero de instancias = multi x n_instances")
    args = parser.parse_args()
    print(args.multi)
    
    try:
        device_manager = DeviceManager()
        
        #register signal handlers
        signal.signal(signal.SIGINT, lambda sig, frame: signal_handler(sig, frame, device_manager))
        signal.signal(signal.SIGBREAK, lambda sig, frame: signal_handler(sig, frame, device_manager))
      
        
        for _ in range(args.n_instances):
            if args.multi:
                
                sensor_list = args.multi.split(',')
                device_manager.start_multiple_devices(sensor_list,args.time_interval)
            
            elif args.n_instances:
                print("Starting single device")
                device_manager.start_single_device(device_type=args.device_type,interval_s=args.time_interval)
            
        while True:
            time.sleep(100)
            
    except KeyboardInterrupt:
        print("IoT Hub client stopped")
    finally:
        # Gracefully shutdown the client
        device_manager.stop_all_devices()

if __name__ == "__main__":
    main()