def update_libro_stok(sender, instance, **kwargs):
    # actualizamos el stock si se elimina un prestamo
    instance.libro.stok = instance.libro.stok + 1
    instance.libro.save()