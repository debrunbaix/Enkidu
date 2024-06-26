
void _fini(void)

{
  __do_global_dtors_aux();
  return;
}

