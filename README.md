<h1>File organizer</h1>
 
 
 
 File organizer é um software organizador da pasta de Download.
Foi desenvolvido com o intuito de organizar os arquivo abaixados, organizando para um diretório apropriado.


- Este <strong>README</strong> e todos os sub-documentos presentes aqui tem como objetivo guiar a estrutura deste projeto e devem auxiliar na escalabilidade das funcionalidades existentes hoje e nas que serão criadas com o decorrer do andamento do projeto.

- Este programa foi desenvolvido para sistema Linux. Testado em <strong>Ubuntu, Pop_os, Linux Mint</strong>. Tendo como base de fucionamento o <strong>Debian.</strong>

----
 
<h2>Instalação</h2>

Para poder execultar o programa na sua máquina é necessário ter instalado certas bibliotecas para um funcionamento correto.

Mas você pode poupar tempo instalando manualmente, usando o  <a href="https://github.com/thisiscleverson/installer-fileOrginazer.git">instalador.</a>

-  instalando as bibliotecas do programa.
 ```
 pip3 install notify2
 ```

```
 pip3 install pyinotify
```

```
 pip3 install playsound
```

- instalando o pyinstaller

	instale o <strong>pyinstaller</strong> para transformar o programa como execultavel.
	
	```
	pip3 install pyinstaller
	```
	

- transformando o programa para um execultavel
	
	1. abra o arquivo <code>file-organizer</code>.
		<p>
			<img src="/src/assets/file-organizer-img.jpg">
		</p>
	2. abra o terminal e execulte o comando:
		```
		pyinstaller --onefile --noconsole File_Organizer.py
		```
		<p>
			<img src="/src/assets/terminal.jpg">
		</p>
	3. abra o aplicativo <strong>startup applications</strong> -em português- <strong>aplicativos de inicialização</strong> e adicione o programa no diretorio 
		```
		./file-organizer/dist/File_Organizer
		```
		<p>
			<img src="/src/assets/startup-applications.jpg">
		</p>
		<p>
			<img src="/src/assets/startup-applications-add.jpg">
		</p>
	4. reinicie sua máquina.
	
		quando o programa for iniciado, vai aparecer uma notificação.
		<p>
			<img src="/src/assets/notify.jpg">
		</p>
	




 
 