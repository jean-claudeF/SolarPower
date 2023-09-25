from sh1106 import SH1106_I2C, SH1106

class OLED(SH1106_I2C):
   
    def __init__(self, width, height, i2c, res=None, addr=0x3c,
                 rotate=0, external_vcc=False):     
        self.currentline = 0
        self.maxline = 5
        
        self.i2c = i2c
        self.addr = addr
        self.res = res
        
        # init base class:
        SH1106_I2C.__init__(self, width, height, i2c, res = res, addr=addr,
                 rotate=rotate, external_vcc=external_vcc)
        
        
    def clear(self):
        self.fill(0)
        self.currentline = 0
    
        
    def text(self, text, x, y):
        self.text(text, x, y)
        
    def write_line(self, text, line):
        '''write text to OLED into line 0...5'''
        self.text(text, 0, line * 10)
        self.show()


    def print(self, text, autoclear = True):
        '''print string s to OLED and automatically go to next row
           with clear before line 0'''
        if self.currentline == 0:
            if autoclear == True:
                self.fill(0)
                
        self.write_line(text,  self.currentline )
        self.currentline += 1
        if self.currentline > self.maxline:
            self.currentline = 0
    
    
        
    def print_s(self, s, separator = '\t'):
        '''print string s to OLED
        s -> multiple rows, separated by '\t'   '''
        
        sarray = s.split(separator)
        self.fill(0)
        self.currentline = 0
        for item in sarray:
            #self.print(item)
            self.text(item, 0, self.currentline * 10)
            self.currentline += 1
            if self.currentline > self.maxline:
                self.currentline = 0
        self.show()    

        
if __name__ == "__main__":
    from machine import Pin, I2C
    import time


    i2c = I2C(0, scl=Pin(9), sda=Pin(8))
    #oled = SH1106_I2C(128, 64, i2c)
    oled = OLED(128, 64, i2c, rotate = 180)
    
    def test1():
        oled.clear()
        oled.print("TEST OLED PRINT")
        for i in range(0,8):
            #oled.print_line("TEST " + str(i))
            oled.print("TEST " + str(i))
            time.sleep(0.2)
            oled.show()

    def test2():
        oled.clear()

        oled.text("TEST OLED", 0, 0)      # text, x, y, colour (1 = white)     
        #oled.text("TEST OLED",5,5)
        oled.text("by JCF",5,15)
        oled.text("Another row", 5, 25)
        oled.text("Yet another row", 5, 35)
        oled.text("And one more", 5, 45)
        oled.show()



    def test3():
        oled.clear()
        oled.text("TEST ", 30, 0)             
        oled.hline(10,10, 20, 1)
        oled.vline(10, 20, 30, 1)
        oled.line(10, 10, 50, 50, 1)
        oled.rect(20, 20, 60, 40, 1)
        oled.fill_rect(80, 20, 20, 20, 1)
        oled.show()



    def test4():
        oled.clear()
        for i in range(0,6):
            #oled.print_line("TEST LINE" + str(i))
            oled.print("TEST LINE" + str(i))
        oled.show()               

    def test5():
        s = "Hello \t world \t ! \t 3.14     \t The answer is \t 42"
        oled.print_s(s)
        '''
        time.sleep(1)
        s = "123456789 \t ! \t 3.14     \t The answer is \t 42\t Hitchhiker"
        oled.print_s(s) 
        '''
        
    def test_all():
        test1()
        time.sleep(1)
        test2()
        time.sleep(1)
        test3()
        time.sleep(1)
        test4()
        time.sleep(1)
        test5()
        time.sleep(1)
        
    
    test_all()
    #test5()
    