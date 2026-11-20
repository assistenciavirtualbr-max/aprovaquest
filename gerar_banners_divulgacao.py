import os
from PIL import Image, ImageDraw, ImageFont

FONTS_DIR = r"C:\Windows\Fonts"
FONT_BOLD = os.path.join(FONTS_DIR, "segoeuib.ttf")
FONT_REGULAR = os.path.join(FONTS_DIR, "segoeui.ttf")

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def draw_gradient_rect(draw, bbox, c1, c2, vertical=True):
    x0, y0, x1, y1 = bbox
    h = y1 - y0
    w = x1 - x0
    for i in range(h if vertical else w):
        ratio = i / float(h if vertical else w)
        r = int(c1[0] + (c2[0] - c1[0]) * ratio)
        g = int(c1[1] + (c2[1] - c1[1]) * ratio)
        b = int(c1[2] + (c2[2] - c1[2]) * ratio)
        if vertical:
            draw.line([(x0, y0 + i), (x1, y0 + i)], fill=(r, g, b))
        else:
            draw.line([(x0 + i, y0), (x0 + i, y1)], fill=(r, g, b))

def gerar_banner_quadrado(output_path):
    w, h = 1080, 1080
    img = Image.new("RGB", (w, h), (15, 23, 42)) # Slate 900
    draw = ImageDraw.Draw(img)

    # Background gradient
    draw_gradient_rect(draw, (0, 0, w, h), (15, 23, 42), (30, 27, 75)) # Slate 900 to Indigo 950

    # Top Tag
    f_tag = get_font(FONT_BOLD, 26)
    tag_text = "🎓 TESTE GRATUITO PARA CONCURSEIROS NO CELULAR"
    tag_w = draw.textlength(tag_text, font=f_tag)
    pill_x0 = (w - tag_w) // 2 - 25
    pill_y0 = 60
    pill_x1 = pill_x0 + tag_w + 50
    pill_y1 = pill_y0 + 55
    draw.rounded_rectangle([pill_x0, pill_y0, pill_x1, pill_y1], radius=28, fill=(79, 70, 229)) # Brand Indigo
    draw.text((pill_x0 + 25, pill_y0 + 10), tag_text, font=f_tag, fill=(255, 255, 255))

    # Big Title
    f_title1 = get_font(FONT_BOLD, 54)
    f_title2 = get_font(FONT_BOLD, 62)
    t1 = "CHEGA DE MENSALIDADES DE R$ 50"
    t2 = "E APPS LOTADOS DE ANÚNCIOS!"
    draw.text(((w - draw.textlength(t1, font=f_title1)) // 2, 160), t1, font=f_title1, fill=(241, 245, 249))
    draw.text(((w - draw.textlength(t2, font=f_title2)) // 2, 230), t2, font=f_title2, fill=(251, 191, 36)) # Amber gold

    # Subtitle
    f_sub = get_font(FONT_REGULAR, 32)
    sub1 = "Conheça o AprovaQuest: O Aplicativo de Questões Comentadas"
    sub2 = "focado em Lei Seca, Súmulas e Pegadinhas das Bancas"
    draw.text(((w - draw.textlength(sub1, font=f_sub)) // 2, 320), sub1, font=f_sub, fill=(203, 213, 225))
    draw.text(((w - draw.textlength(sub2, font=f_sub)) // 2, 365), sub2, font=f_sub, fill=(203, 213, 225))

    # 4 Benefits Boxes (2x2 Grid)
    box_w, box_h = 470, 150
    spacing = 30
    start_x = (w - (2 * box_w + spacing)) // 2
    start_y = 440

    benefits = [
        ("📱 INSTALA NO CELULAR", "Roda direto no Android ou iPhone em tela cheia como app nativo.", (16, 185, 129)),
        ("⚡ 100% OFFLINE", "Resolva questões no ônibus, metrô ou intervalo sem precisar de internet.", (56, 189, 248)),
        ("⚖️ LEI SECA & SÚMULAS", "Comentários alternativa por alternativa com o artigo e súmula da questão.", (245, 158, 11)),
        ("🚫 ZERO PROPAGANDAS", "Estudo ativo com cronômetro, caderno de erros e mentor com inteligência artificial.", (168, 85, 247))
    ]

    f_box_t = get_font(FONT_BOLD, 26)
    f_box_d = get_font(FONT_REGULAR, 20)

    for i, (b_title, b_desc, col) in enumerate(benefits):
        bx = start_x + (i % 2) * (box_w + spacing)
        by = start_y + (i // 2) * (box_h + spacing)

        # Card container
        draw.rounded_rectangle([bx, by, bx + box_w, by + box_h], radius=20, fill=(30, 41, 59), outline=(71, 85, 105), width=2)
        # Left border accent
        draw.rounded_rectangle([bx, by, bx + 10, by + box_h], radius=5, fill=col)
        # Title
        draw.text((bx + 25, by + 20), b_title, font=f_box_t, fill=col)
        # Description (multi-line)
        draw.text((bx + 25, by + 65), b_desc[:42], font=f_box_d, fill=(226, 232, 240))
        draw.text((bx + 25, by + 95), b_desc[42:].strip(), font=f_box_d, fill=(148, 163, 184))

    # Bottom Offer Container
    bot_y = 810
    draw.rounded_rectangle([60, bot_y, w - 60, bot_y + 210], radius=28, fill=(17, 24, 39), outline=(16, 185, 129), width=3)

    # CTA Button
    f_cta = get_font(FONT_BOLD, 36)
    cta_txt = "📲 TESTAR GRÁTIS NO CELULAR AGORA"
    draw.rounded_rectangle([100, bot_y + 25, w - 100, bot_y + 105], radius=20, fill=(16, 185, 129))
    draw.text(((w - draw.textlength(cta_txt, font=f_cta)) // 2, bot_y + 42), cta_txt, font=f_cta, fill=(255, 255, 255))

    # Link & Promo text
    f_link = get_font(FONT_BOLD, 26)
    f_promo = get_font(FONT_REGULAR, 22)
    link_txt = "👉 assistenciavirtualbr-max.github.io/aprovaquest"
    promo_txt = "Oferta de Lançamento: Acesso Vitalício por apenas R$ 29,90 (sem mensalidade!)"
    draw.text(((w - draw.textlength(link_txt, font=f_link)) // 2, bot_y + 120), link_txt, font=f_link, fill=(56, 189, 248))
    draw.text(((w - draw.textlength(promo_txt, font=f_promo)) // 2, bot_y + 160), promo_txt, font=f_promo, fill=(148, 163, 184))

    img.save(output_path, quality=95)
    print(f"Generated: {output_path}")

def gerar_banner_stories(output_path):
    w, h = 1080, 1920
    img = Image.new("RGB", (w, h), (15, 23, 42))
    draw = ImageDraw.Draw(img)

    draw_gradient_rect(draw, (0, 0, w, h), (15, 23, 42), (30, 27, 75))

    # Top Tag
    f_tag = get_font(FONT_BOLD, 30)
    tag_text = "🎓 DICA DE OURO PARA CONCURSEIROS"
    tag_w = draw.textlength(tag_text, font=f_tag)
    pill_x0 = (w - tag_w) // 2 - 30
    draw.rounded_rectangle([pill_x0, 120, pill_x0 + tag_w + 60, 185], radius=32, fill=(79, 70, 229))
    draw.text((pill_x0 + 30, 132), tag_text, font=f_tag, fill=(255, 255, 255))

    # Big Title
    f_t1 = get_font(FONT_BOLD, 64)
    f_t2 = get_font(FONT_BOLD, 68)
    draw.text(((w - draw.textlength("PARE DE PAGAR R$ 50/MÊS", font=f_t1)) // 2, 240), "PARE DE PAGAR R$ 50/MÊS", font=f_t1, fill=(255, 255, 255))
    draw.text(((w - draw.textlength("EM PLATAFORMAS DE QUESTÕES!", font=f_t2)) // 2, 330), "EM PLATAFORMAS DE QUESTÕES!", font=f_t2, fill=(251, 191, 36))

    # Central Phone Mockup Card
    mock_w, mock_h = 860, 780
    mock_x = (w - mock_w) // 2
    mock_y = 460
    draw.rounded_rectangle([mock_x, mock_y, mock_x + mock_w, mock_y + mock_h], radius=36, fill=(30, 41, 59), outline=(71, 85, 105), width=3)

    # Phone Inner Card
    f_app_t = get_font(FONT_BOLD, 34)
    draw.text((mock_x + 40, mock_y + 35), "AprovaQuest • Concursos Públicos", font=f_app_t, fill=(255, 255, 255))
    draw.rounded_rectangle([mock_x + mock_w - 200, mock_y + 30, mock_x + mock_w - 40, mock_y + 75], radius=15, fill=(16, 185, 129))
    f_off = get_font(FONT_BOLD, 22)
    draw.text((mock_x + mock_w - 180, mock_y + 40), "100% OFFLINE", font=f_off, fill=(255, 255, 255))

    items = [
        ("📱 Instala direto no celular como Aplicativo Nativo", (56, 189, 248)),
        ("⚖️ Análise completa: Artigo de Lei Seca + Súmula", (245, 158, 11)),
        ("🔍 Por que a certa está certa e por que a errada é errada", (16, 185, 129)),
        ("⏱️ Simulados cronometrados com nota de corte oficial", (168, 85, 247)),
        ("🚫 Zero propagandas, sem pegadinhas de cobrança mensal", (244, 63, 94)),
        ("🤖 Mentor IA com Macetes e Mnemônicos 24h", (251, 191, 36))
    ]

    f_item = get_font(FONT_BOLD, 26)
    for idx, (txt, col) in enumerate(items):
        iy = mock_y + 120 + idx * 105
        draw.rounded_rectangle([mock_x + 35, iy, mock_x + mock_w - 35, iy + 85], radius=18, fill=(15, 23, 42))
        draw.ellipse([mock_x + 60, iy + 25, mock_x + 95, iy + 60], fill=col)
        draw.text((mock_x + 115, iy + 25), txt, font=f_item, fill=(241, 245, 249))

    # Pricing & CTA Box
    cta_y = 1320
    draw.rounded_rectangle([80, cta_y, w - 80, cta_y + 460], radius=40, fill=(17, 24, 39), outline=(16, 185, 129), width=4)

    f_prc_sub = get_font(FONT_REGULAR, 30)
    draw.text(((w - draw.textlength("De R$ 97,00 por apenas:", font=f_prc_sub)) // 2, cta_y + 40), "De R$ 97,00 por apenas:", font=f_prc_sub, fill=(148, 163, 184))

    f_prc = get_font(FONT_BOLD, 80)
    draw.text(((w - draw.textlength("R$ 29,90", font=f_prc)) // 2, cta_y + 90), "R$ 29,90", font=f_prc, fill=(16, 185, 129))

    f_vit = get_font(FONT_BOLD, 30)
    draw.text(((w - draw.textlength("PAGAMENTO ÚNICO • ACESSO VITALÍCIO", font=f_vit)) // 2, cta_y + 200), "PAGAMENTO ÚNICO • ACESSO VITALÍCIO", font=f_vit, fill=(251, 191, 36))

    # Big CTA Button
    f_btn = get_font(FONT_BOLD, 38)
    draw.rounded_rectangle([120, cta_y + 260, w - 120, cta_y + 360], radius=25, fill=(16, 185, 129))
    draw.text(((w - draw.textlength("TOQUE PARA TESTAR GRÁTIS", font=f_btn)) // 2, cta_y + 285), "TOQUE PARA TESTAR GRÁTIS", font=f_btn, fill=(255, 255, 255))

    f_link_bot = get_font(FONT_BOLD, 28)
    draw.text(((w - draw.textlength("assistenciavirtualbr-max.github.io/aprovaquest", font=f_link_bot)) // 2, cta_y + 395), "assistenciavirtualbr-max.github.io/aprovaquest", font=f_link_bot, fill=(56, 189, 248))

    img.save(output_path, quality=95)
    print(f"Generated: {output_path}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    gerar_banner_quadrado(os.path.join(base_dir, "BANNER_GRUPOS_FEED_1080x1080.jpg"))
    gerar_banner_stories(os.path.join(base_dir, "BANNER_STORIES_STATUS_1080x1920.jpg"))

if __name__ == "__main__":
    main()
