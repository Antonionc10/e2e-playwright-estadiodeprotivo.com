from playwright.sync_api import Page, expect

def test_visit(page: Page):
    print("Given user visit homepage")
    page.goto("https://estadiodeportivo.com")

def test_signup_empty_email(page:Page):
    page.goto("https://www.estadiodeportivo.com/")
    
    page.get_by_role("email").clear()
    
    page.get_by_role("textbox").first.clear()
    page.get_by_role("textbox").first.press("CapsLock")
    page.get_by_role("textbox").first.fill("A")
    page.get_by_role("textbox").first.press("CapsLock")
    page.get_by_role("textbox").first.fill("Antonio")
    
    page.get_by_text("Crear cuenta").click()
    page.get_by_role("checkbox", name="He leído y acepto los té").check()
    page.get_by_text("INICIAR SESIÓNREGÍSTRATE¿").click()
    
    page.get_by_role("img", name="Mostrar contraseña").clear()
    page.get_by_role("img", name="Ocultar contraseña").click()
    
    page.get_by_text("Bienvenid@ a Estadio Deportivo").click()
    expect(page.locator("body")).to_contain_text("Bienvenid@ a Estadio Deportivo")
    

def test_signup_empty_password(page:Page):
    page.goto("https://www.estadiodeportivo.com/")
    
    page.get_by_role("button", name="Rechazar").click()
    page.get_by_role("banner").locator("svg").click()
    
    page.get_by_text("REGÍSTRATE", exact=True).click()
    page.get_by_role("textbox").first.clear()
    page.get_by_role("textbox").first.fill("Antonio")
   
    page.get_by_role("textbox").nth(1).clear()
    page.get_by_role("textbox").nth(1).fill("antonio@gmail.com")
    
    page.get_by_role("checkbox", name="He leído y acepto los té").check()
    page.locator("#btn-login").click()
    expect(page.get_by_text("Crear cuenta")).to_be_visible()
    expect(page.get_by_text("Bienvenid@ a Estadio Deportivo")).to_be_visible()
    expect(page.locator("body")).to_contain_text("Bienvenid@ a Estadio Deportivo")