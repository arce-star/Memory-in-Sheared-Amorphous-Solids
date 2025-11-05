# Memory-in-Sheared-Amorphous-Solids

存放该项目的标准代码

## 代码列表

- `in.LJ` 制备 BMLJ 粒子体系  
  生成一个 BMLJ_1.data 位形文件
- `in.shear` 对制备出的粒子体系进行指定轮次的剪切振荡训练  
  输入 BMLJ_1.data 位形文件，输出每轮次训练后的位形文件 sheared_oscillation_1.data...sheared_oscillation_20.data
- `in.read` 对训练某轮次后的体系进行独立的不同振幅读取  
  输入训练某轮次后的体系位形文件 sheared_oscillation_1.data ，输出这个位形在不同振幅下读取的 MSD 文件 Amplitude_MSD_data.txt
- `in.read_one` 对训练某轮次后的体系进行独立的单振幅读取
  输入训练某轮次后的体系位形文件 sheared_oscillation_5.data ，输出这个位形在0.06振幅下读取的 MSD 文件 Amplitude_MSD_data.txt
- `in.yield` 对一个位形进行单向剪切并测量应力应变曲线
  输入体系位形文件 BMLJ_03.data ，输出这个位形在从0应变到0.3应变过程中的 strain-stress 数据文件 stress_strain_bmlj.txt

## 命令行命令

详见 `bat.txt` 文件注释
