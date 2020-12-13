# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['InterfaceGrafica.py'],
             pathex=['C:\\Users\\joabs\\Documents\\Engenharia de Computação\\Cursos\\Periodo 6\\Inteligência Artificial\\Projeto Sudoku'],
             binaries=[],
             datas=[("sonsdojogo", "sonsdojogo")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='InterfaceGrafica',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
