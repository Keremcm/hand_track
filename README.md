# English
# Hand-Tracking Mouse Control Using OpenCV, MediaPipe, and PyAutoGUI

This project allows you to control the mouse using hand gestures tracked through a webcam. By leveraging OpenCV for video capture, MediaPipe for hand tracking, and PyAutoGUI for controlling the mouse and keyboard, this system enables gesture-based interaction with your computer.

## Features
- **Move the mouse cursor** by tracking the index finger.
- **Left-click** by bringing the index finger and thumb together.
- **Right-click** by bringing the middle finger and thumb together.
- **Undo (Ctrl+Z)** by bringing the ring finger and thumb together.
- **Alt+Tab** to switch between windows by bringing the pinky finger and thumb together.

## Dependencies

To run this project, you'll need the following Python libraries:

- `opencv-python`
- `mediapipe`
- `numpy`
- `pyautogui`
- `pygetwindow`

You can install them using pip:

```bash
pip install opencv-python mediapipe numpy pyautogui pygetwindow
```

## How It Works
Camera Input: The webcam captures real-time video and uses MediaPipe to detect hand landmarks.
Gesture Detection: Key points like the thumb and finger tips are identified to perform gestures.
Mouse Control: Hand gestures are mapped to specific actions like mouse movement, clicks, undo operations, and window switching.
Smoothing: The movement of the cursor is smoothed to make it more natural and avoid sudden jumps.

## Usage
Clone the repository:
```bash
git clone https://github.com/Keremcm/hand_track.git
```

Navigate to the project directory:
```bash
cd hand-track
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Run the script:
```bash
python hand_track.py
```

Use your hand in front of the camera to control the mouse and perform various actions as described above.

## Customization
Sensitivity: You can adjust the sensitivity and responsiveness by changing the threshold values for finger distances or modifying the map_camera_to_screen function for more fine-tuned cursor control.
Additional Gestures: You can add more gestures by analyzing other hand landmarks provided by MediaPipe.

## Notes
Make sure to adjust your webcam resolution for optimal performance.
The default webcam is used, but you can change the cap object to point to a different camera if needed.

## License
You can modify the sections to fit the specifics of your project. Let me know if you'd like further customization!

# İngilizce
# OpenCV, MediaPipe ve PyAutoGUI Kullanarak Elle Takip Edilen Fare Kontrolü

Bu proje, bir web kamerası aracılığıyla takip edilen el hareketlerini kullanarak fareyi kontrol etmenize olanak tanır. Video yakalama için OpenCV'den, el izleme için MediaPipe'dan ve fare ve klavyeyi kontrol etmek için PyAutoGUI'den yararlanan bu sistem, bilgisayarınızla jest tabanlı etkileşime olanak tanır.

## Özellikler
- **İşaret parmağını takip ederek fare imlecini hareket ettirin**.
- **İşaret parmağını ve başparmağı bir araya getirerek **sol tıklayın**.
- **Orta parmakla başparmağı bir araya getirerek **sağ tıklayın**.
- **Yüzük parmağını ve başparmağı bir araya getirerek geri alın (Ctrl+Z)**.
- Serçe parmağınızı ve baş parmağınızı bir araya getirerek pencereler arasında geçiş yapmak için **Alt+Tab**.

## Bağımlılıklar

Bu projeyi çalıştırmak için aşağıdaki Python kitaplıklarına ihtiyacınız olacak:

- 'opencv-python'
- 'mediapipe'
- 'numpy'
- 'pyautogui'
- 'pygetwindow'

Bunları pip kullanarak yükleyebilirsiniz:

```bash
pip install opencv-python mediapipe numpy pyautogui pygetwindow
```

## Nasıl Çalışır?
Kamera Girişi: Web kamerası gerçek zamanlı video çeker ve el yer işaretlerini tespit etmek için MediaPipe'ı kullanır.
Hareket Algılama: Hareketleri gerçekleştirmek için başparmak ve parmak uçları gibi önemli noktalar tanımlanır.
Fare Kontrolü: El hareketleri, fare hareketi, tıklamalar, geri alma işlemleri ve pencere değiştirme gibi belirli eylemlerle eşleştirilir.
Yumuşatma: İmlecin hareketi, daha doğal hale getirilmesi ve ani sıçramaların önlenmesi için yumuşatılır.

## Kullanım
Depoyu klonlayın:
``` bash
git klonu https://github.com/Keremcm/hand_track.git
```

Proje dizinine gidin:
``` bash
cd hand-track
```

Gerekli bağımlılıkları yükleyin:
``` bash
pip install -r requiments.txt
```

## Komut dosyasını çalıştırın:
``` bash
python hand_track.py
```

Fareyi kontrol etmek ve yukarıda açıklandığı gibi çeşitli eylemleri gerçekleştirmek için elinizi kameranın önünde kullanın.

## Kişiselleştirme
Hassasiyet: Parmak mesafeleri için eşik değerlerini değiştirerek veya daha hassas ayarlanmış imleç kontrolü için map_camera_to_screen işlevini değiştirerek hassasiyeti ve yanıt verme hızını ayarlayabilirsiniz.
Ek Hareketler: MediaPipe tarafından sağlanan diğer el işaretlerini analiz ederek daha fazla hareket ekleyebilirsiniz.

## Notlar
Optimum performans için web kameranızın çözünürlüğünü ayarladığınızdan emin olun.
Varsayılan web kamerası kullanılır, ancak gerekirse kapak nesnesini farklı bir kamerayı işaret edecek şekilde değiştirebilirsiniz.

## Lisans
Bölümleri projenizin özelliklerine uyacak şekilde değiştirebilirsiniz. Daha fazla özelleştirme istiyorsanız bana bildirin!
