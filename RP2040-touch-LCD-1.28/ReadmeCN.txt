/*****************************************************************************
* | File      	:   Readme_CN.txt
* | Author      :   
* | Function    :   Help with use
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2022-06-23
* | Info        :   在这里提供一个中文版本的使用文档，以便你的快速使用
******************************************************************************/
这个文件是帮助您使用本例程。
在这里简略的描述本工程的使用：

1.基本信息：
本例程使用RP2040-LCD-1.28进行了验证，你可以在工程的中查看对应的测试例程;

2.管脚连接：
管脚连接你可以在RP2040-LCD-1.28.py查看，这里也再重述一次：

I2C_SDA     ->      6
I2C_SDA     ->      7
DC          ->      8
CS          ->      9
SCK         ->      10
DIN         ->      11
RST         ->      12  
BL          ->      25
BAT_ADC     ->      29


3.基本使用：
    1): 按住Pico板上的按键，将pico通过Micro USB线接到电脑的USB接口，然后松开按键。
        接入之后，电脑会自动识别到一个可移动盘（RPI-RP2）
        
    2): 将python目录中rp2-pico-20220117-v1.18.uf2 文件复制到识别的可移动盘（RPI-RP2）中
    
    3): 更新Thonny IDE
        sudo apt upgrade thonny
        
    4): 打开Thonny IDE （点击树莓logo -> Programming -> Thonny Python IDE ）
        选择Tools -> Options... -> Interpreter
        选择MicroPython(Raspberry Pi Pico 和ttyACM0端口
        
    5): 在Thonny IDE中打开python/RP2040-LCD-1.28/RP2040-LCD-1.28.py文件
        然后运行当前脚本（绿色小三角）即可
    