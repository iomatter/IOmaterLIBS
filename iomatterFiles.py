#  copyright, (C) IOmatter INC.
def file(use, path, data) {
 fileOS = open(path, use)
  if use == 'u' or 'a':
    fileOS.write(data)
    ''' USEAGE:
    file('a', 'text.txt', 'Hello!')
    '''
}
