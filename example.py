import libnodave

link = libnodave.libnodave()

def main():

  localMPI = 0
  plcMPI = 2 #anpassen, je nach CPU Adresse
  plcRack = 0
  plcSlot = 0

  #link.SetDebug(99)

  link.set_port(b'/dev/ttyUSB0', b'38400', b'O')
       
  link.new_interface(b'IF1', localMPI, libnodave.daveProtoMPI, libnodave.daveSpeed187k)

  link.set_timeout(3000000)

  link.init_adapter()   

  link.connect_plc(plcMPI, plcRack, plcSlot)   
 
  print('*****SINGOLI BIT - BOOL*******') 
  
  print('M0.0 è', link.get_marker(0,0))   
  print('M0.1 è', link.get_marker(0,1))
  print('M0.2 è', link.get_marker(0,2))
  print('M0.3 è', link.get_marker(0,3))
  print('M0.4 è', link.get_marker(0,4))
  print('M0.5 è', link.get_marker(0,5))
  print('M0.6 è', link.get_marker(0,6))
  print('M0.7 è', link.get_marker(0,7))
  
  print('\n*****SINGOLI BYTE*******')
  
  print('byte M1 come int', link.get_marker_byte(1))
  print('byte M1 come bit arr', link.get_marker_byte_list(1))
  print('byte M1 come bit:valore', link.get_marker_byte_dict(1))
  
  print('\n*****USCITE SINGOLE E COME BYTE*******')
  
  print('bit di output A0.0 è', link.get_output(0,0))
  print('byte di output A0 è', libnodave.int_to_bitarr(link.get_output_byte(0)))
  
  print('\n*****2 BYTE - MW*******')
  
  if (link.read_bytes(0x83, 0, 50, 2)):
    for x in range(2):
      itm = link.dave.daveGetU8(link.dc)
      print('itm', libnodave.int_to_bitarr(itm))
    
  print('\n*****4 BYTE - MD*******')
  
  if (link.read_bytes(0x83, 0, 50, 4)):
    for x in range(4):
      itm = link.dave.daveGetU8(link.dc)
      print('itm', libnodave.int_to_bitarr(itm))

  print('\n*****DB - DB n°, da BYTE x, per N BYTES (in base 10)*******') 
  
  DBnum = 2
  FirtsByte = 0
  HowManyByte = 2
  risp = link.get_db_byte(DBnum, FirtsByte, HowManyByte)
  if risp != 'ko':
    print('Leggo DB 2 byte 0 per 2 byte', risp)
  else:
    print('richiesta errata')
  
  print('\n*****DB - DB n°, da BYTE x, per N BYTES (in bit array)*******') 
  
  DBnum = 2
  FirtsByte = 0
  HowManyByte = 10
  if (link.read_bytes(0x84, DBnum, FirtsByte, HowManyByte)):
    for x in range(HowManyByte):
      itm = link.dave.daveGetU8(link.dc)
      print('itm', libnodave.int_to_bitarr(itm))
  else:
    print('richiesta errata')
    
  print('\n*****ottieni intero (2byte) da DB*******')  
  
  risp = link.get_int_db(2, 0)
  if risp != 'ko':
    print('DB2.DBW0 = ', risp)
  else:
    print('richiesta errata')
    
    
  print('\n*****ottieni DINT (4byte) da DB*******')  
  
  risp = link.get_dint_db(2, 2)
  if risp != 'ko':
    print('DB2.DBD2 = ', risp)
  else:
    print('richiesta errata')
  
  print('\n*****ottieni intero (2byte) da MEMORIA*******')  
  
  risp = link.get_int_mem(60)
  if risp != 'ko':
    print('MW60 = ', risp)
  else:
    print('richiesta errata')
  
  print('\n*****ottieni DINT (4byte) da MEMORIA*******')  
  
  risp = link.get_dint_mem(62)
  if risp != 'ko':
    print('MW62 = ', risp)
  else:
    print('richiesta errata') 
    
  print('\n*****ottieni REAL (4byte) da DB*******')  
  
  risp = link.get_real_db(2, 6)
  if risp != 'ko':
    print('DB2.DBD6 = ', risp)
  else:
    print('richiesta errata')
    
  print('\n*****ottieni REAL (4byte) da MEMORIA*******')  
  
  risp = link.get_real_mem(66)
  if risp != 'ko':
    print('MD66 = ', risp)
  else:
    print('richiesta errata')
  

  
  link.disconnect()

if __name__ == "__main__":
  main()
