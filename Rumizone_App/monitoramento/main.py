# CARREGA AS DEPENDENCIAS
import cv2
import time


def monitoramento(camera):
    # CARREGA O VIDEO
    video_vacas = camera

    
    # CORES DAS CLASSES
    color = (0, 255, 255)

    # CARREGA AS CLASSES
    class_names = []
    with open("monitoramento/coco.names", "r") as f:
        class_names = [cname.strip() for cname in f.readlines()]

    # CAPTURA DO VIDEO
    cap = cv2.VideoCapture(video_vacas)

    # CARREGANDO OS PESOS DA REDE NEURAL
    net = cv2.dnn.readNet("monitoramento/yolov4-tiny.cfg", "monitoramento/yolov4-tiny.weights",)

    # SETANDO OS PARAMETROS DA REDE NEURAL
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(416, 416), scale=1 / 255)

    # LENDO OS FRAMES DO VIDEO
    while True:
        # Leia um quadro do vídeo
        ret, frame = cap.read()

        # COMEÇO DA CONTAGEM DOS MS
        start = time.time()

        # DETECÇÃO
        classes, scores, boxes = model.detect(frame, 0.1, 0.2)

        # FIM DA CONTAGEM DOS MS
        end = time.time()

        # PERCORRER TODAS AS DETECÇÕES
        for (classid, score, box) in zip(classes, scores, boxes):
            # PEGANDO O NOME DA CLASSE PELO ID E SEU SCORE DE ACURÁCIA
            label = f"{class_names[classid]} : {score}"

            # DESENHANDO A BOX DA DETECÇÃO
            if class_names[classid] == "cow":
                cv2.rectangle(frame, box, color, 2)

            # ESCREVENDO O NOME DA CLASSE EM CIMA DA BOX DO OBJETO
            if class_names[classid] == "cow":
                cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # CALCULANDO O TEMPO QUE LEVOU PARA FAZER A DETECÇÃO
            fps_label = f"FPS: {round((1.0 / (end - start)), 2)}"

            # ESCREVENDO O FPS NA IMAGEM
            cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5)
            cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        # Verifique se a leitura do quadro foi bem-sucedida
        if not ret:
            break

        # Exiba o quadro
        cv2.imshow("video_vacas", frame)

        # Pressione a tecla 'q' para sair do loop
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    # Libere o objeto de captura e feche a janela de exibição
    cap.release()
    cv2.destroyAllWindows()
    
