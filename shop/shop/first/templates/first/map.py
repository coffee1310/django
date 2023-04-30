import folium

m=folium.Map(width= 950, height=550, zoom_start=10, location=[55.76766184702502, 37.594135589055654], position='toprigth')

folium.Marker([55.75539761094001, 37.61795604341731], popup="Мавзолей Ленина", tooltip="Мавзолей Ленина").add_to(m)
folium.Marker([55.77163863385089, 37.64179166339341], popup="M.Видео", tooltip="M.Видео").add_to(m)
folium.Marker([55.69778019769173, 37.600285043934676], popup="ГБУЗ НИКИО им. Л.И. Свержевского ДЗМ", tooltip="ГБУЗ НИКИО им. Л.И. Свержевского ДЗМ").add_to(m)
folium.Marker([55.56843828060165, 37.46572415039861], popup="Городская клиническая больница №40", tooltip="Городская клиническая больница №40").add_to(m)
folium.Marker([55.75643781261594, 37.54146936004568], popup="ДГКБ №9 им. Г. Н. Сперанского", tooltip="ДГКБ №9 им. Г. Н. Сперанского").add_to(m)
folium.Marker([55.793124016621405, 37.38832204605409], popup="METRO Cash & Carry", tooltip="METRO Cash & Carry").add_to(m)
folium.Marker([55.84485024241855, 37.383660384180686], popup="ТЦ Митинский радиорынок", tooltip="ТЦ Митинский радиорынок").add_to(m)
folium.Marker([55.890240570394155, 37.5378818347221], popup="ТРЦ Зиг-Заг", tooltip="Мавзолей Ленина").add_to(m)
folium.Marker([55.91913120624165, 37.755883857201425], popup="ТРК Красный кит", tooltip="ТРК Красный кит").add_to(m)
folium.Marker([55.751497418752216, 37.618492737420084], popup="Боровицкая площадь", tooltip="Боровицкая площадь").add_to(m)
folium.Marker([55.72039801865527, 37.626929456519555], popup="Театр Терезы Дуровой", tooltip="Театр Терезы Дуровой").add_to(m)
folium.Marker([55.740480698759605, 37.6716776367469], popup="Мощи святой Матроны", tooltip="Мощи святой Матроны").add_to(m)
folium.Marker([55.73774733998668, 37.716103786488254], popup="Do A Flip", tooltip="Do A Flip").add_to(m)
folium.Marker([55.7939162900569, 37.676828293772154], popup="Батутный центр JUSTUP!", tooltip="Батутный центр JUSTUP!").add_to(m)
folium.Circle(
    radius=25000,
    location=[55.76766184702502, 37.594135589055654],
    popup="Наши магазины",
    color="#3186cc",
    fill=True,
    fill_color='#3186cc'
).add_to(m)


m.save('map.html')