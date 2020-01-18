
# 剣盾自動化の手引
## まえがき
どうも、いつも放送見てます。   
Arduinoで自動化コンを作った手順を書きます。  
参考にした記事があり、かつそれに少し誤りがあるのでそちらを補足する形を取ります  
  
***

- 自分は[こちら](https://qiita.com/chibi314/items/975784f6e951341fc6ce)の記事を読んで自動化機材を作りました。が、あまりにも落とし穴が多いので補足＆自分の選択をここに記します（以下、この記事を「参考記事」と呼ぶ）
- [この記事](https://qiita.com/sobassy/items/cb707e50f2f27a851886)も参考にしましたが、致命的に足りない部分と誤りがあるのでソースコード以外は参考にしないほうが良いです
- アフェリエイトリンクは無いですし突然危険なサイトに飛ぶことも無いはずですが、不安であればシークレットモードを使ったりURLを吟味したりしながら見てください

***

## 前提知識
- Arduino LeonardoのHID機能を利用し、Switchのコントローラーに擬態することで自動化を実現する
- 端末のvid,pidがswitchに登録されていないと接続が弾かれてしまうのでそれらが何故か暴かれているポッ拳コントローラーになりすますことで突破する

- 全体図
	- Switch ←(USBケーブル)→ Arduino←(ケーブル)→USBシリアル変換基板←(USBケーブル)→ PC
- PCからの操作をしない場合はUSBシリアル基盤は不要

## 準備（機材編）
1. [Arduino Leonardo](https://www.switch-science.com/catalog/968/)を買う
	- 互換機でもOK 電源供給は要らないので[ProMicro](https://ht-deko.com/arduino/promicro.html)でOK
	- 自分が買ったのは[これ](https://www.amazon.co.jp/gp/product/B01M6WULAO/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
	- ATmega32u4チップとやらが内蔵されてる物なら多分行ける？
	- [これ](https://www.amazon.co.jp/s?k=Leonardo+Pro+micro&i=industrial&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss_2)の中から良さげのを見繕うと良いと思う

2. USB接続口を増やすための基盤を買う
	- 自分は[これ](https://www.amazon.co.jp/gp/product/B01LXHQIF0/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)を買った

3. 1と2を接続するためのケーブルを買う
	- 自分は[これ](https://www.amazon.co.jp/gp/product/B00J7LFHVU/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)を買った
	- はんだ付けが嫌すぎるので差し込むだけで繋がるテスト用ワイヤを使った（引っ張るとすぐ取れる）が、はんだ付けを厭わないor他にもっと良い手段を知っているのであればそれで良い

4. USBケーブルを買う
	- 自分の環境・買った基盤によって臨機応変に
	- 自分の買った構成の場合、microB←→USB-Aを2本とUSB-AをUSB-Cに変換するコネクタを使った
	- Dockを使ってる場合は多分1本は両側USB-Aの物にすべき

## 手順1
- [参考記事](https://qiita.com/chibi314/items/975784f6e951341fc6ce)通りでOK
- 上記構成の場合、穴の横の表記を見ながら参考記事の図の通りにテスト用ワイヤをぶっ刺して繋ぐ


## 手順2
[参考記事](https://qiita.com/chibi314/items/975784f6e951341fc6ce) に**一部誤りがある**ので注意

以下参考記事から引用

> 1. Arduino IDEをインストールする
>ここにアクセスし，JUST DOWNLOADを押す．（お財布に余裕のある方はCONTRIBUTE & DOWNLOAD)

>2. Switch操作用ライブラリをインストールする
ここにアクセスし，Clone or download→ Download ZIP
ZIPを解凍し，できたSwitchControlLibrary-masterを[Arduinoがインストールされたディレクトリ]/librariesの中に配置する．


- Arduinoがインストールされたディレクトリは、Win10で設定変えてなければ「C:\Program Files (x86)\Arduino」のこと

>3. Arduino STLをインストールする
>ここから最新のZIPをダウンロードし，解凍する
2と同様に[Arduinoがインストールされたディレクトリ]/librariesの中に配置する


>4. [Arduinoがインストールされたディレクトリ]/hardware/arduino/avr/boards.txtを開き，285, 286行目を以下のように変更する．
- 4について補足
	1. 上の記載は誤り 変更してもArduino端末のvid,pidが書き換わらない 
		- Arduino Studioを起動し、ファイル＞環境設定のパネルの「以下のファイルを直接編集すれば～」の記載の下のパスをクリックするとArduino15というフォルダが開く
		- その中の packages\arduino\hardware\avr\1.8.2
		内にあるboards.txtが正解
	2. 行数指定があるが、自分の環境だと何故だか行数が1行ずれてたのでちゃんと修正箇所の記載を見て適切な場所を書き換えること


>5. Arduinoに書き込むファームウェアをダウンロードする．
>ここにアクセスし，Clone or download→ Download ZIPして解凍
>Arduino IDEを開き，PokemonSWSHAutomation-master\arduino_firmware\pokemon_automation_arduino_firmware\pokemon_automation_arduino_firmware.inoを開く．
- 5について補足
	- そんなパスもファイルも無い
	- firmwareフォルダ内にあるdefault.icoが上に示されてるファイルに対応するのでそちらを使用する

以下記事に補足なし  
参考記事通りで全部OK！

***


## あとがき
- default.icoの代わりに上で[駄目だと書いた記事](https://qiita.com/sobassy/items/cb707e50f2f27a851886)のソースを参考にしながら直接C++コードを書きこめばスタンドアロンで動くシステムになります

- 自分はC++苦手マンなので、Pythonでdefault.icoと通信する用のプログラムを書いてPokemonAutomationの代わりにしています。
	- PCクライアントを自分で作る場合、Baud Rate=115200でシリアル通信を行えば良いです。
	- 例えば、default.icoではAボタンが4,PRESS状態が0と定義されているのでシリアル通信で[4,0]をwriteすればAボタンを押せます。
	- 同じリポジトリ内にpythonファイル置いとくので参考までにどうぞ。
		- jupyter notebook形式のものを変換したものなのでもしかしたらそのままだと動かないかも・・・？
- この文章やその存在については放送で晒したりしても大丈夫です（ガチプロてやんのマジ指摘がちょっと怖いけど・・・😥）。でも、文章ガッタガタかつ他記事を勝手に補足してる関係上あまり拡散しちゃわないようにてやん達には配慮をお願いしたいです。

- そのうち／時間が出来たら／気が向いたらちゃんと記事にしたためたいので、もしそれが実現した暁にはこの手記は消えるかもです。

- 不明点があれば朝以外の放送はだいたい見てますのでどうぞー