import cv2

def extract_chart_regions(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    charts = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w * h > 10000:
            charts.append((x, y, w, h))
    return charts
