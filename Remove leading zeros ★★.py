def remove_leading(ip):
    a = ('.'.join(str(int(part)) for part in ip.split('.')))
    return a