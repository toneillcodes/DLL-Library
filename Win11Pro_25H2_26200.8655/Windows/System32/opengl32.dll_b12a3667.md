# Binary Specification: opengl32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\opengl32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b12a3667ac832b0667418b8a6c0cb107107a5d67d0ac635ed063ac41d0575ede`
* **Total Exported Functions:** 368

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 348 | `wglDeleteContext` | `0x4C30` | 202 | UnwindData |  |
| 361 | `wglShareLists` | `0x4E50` | 518 | UnwindData |  |
| 357 | `wglMakeCurrent` | `0x5060` | 105 | UnwindData |  |
| 347 | `wglCreateLayerContext` | `0x6180` | 591 | UnwindData |  |
| 344 | `wglChoosePixelFormat` | `0x6730` | 1,582 | UnwindData |  |
| 350 | `wglDescribePixelFormat` | `0x6DD0` | 142 | UnwindData |  |
| 362 | `wglSwapBuffers` | `0x7F80` | 100 | UnwindData |  |
| 355 | `wglGetPixelFormat` | `0x84F0` | 296 | UnwindData |  |
| 97 | `glFinish` | `0x86A0` | 64 | UnwindData |  |
| 360 | `wglSetPixelFormat` | `0x86F0` | 922 | UnwindData |  |
| 363 | `wglSwapLayerBuffers` | `0xAB60` | 328 | UnwindData |  |
| 312 | `glTexParameteri` | `0xDF00` | 100 | UnwindData |  |
| 191 | `glNormal3fv` | `0xE9B0` | 6,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `glBitmap` | `0x10150` | 158 | UnwindData |  |
| 83 | `glEndList` | `0x10200` | 61 | UnwindData |  |
| 185 | `glNewList` | `0x10250` | 80 | UnwindData |  |
| 112 | `glGetIntegerv` | `0x102B0` | 86 | UnwindData |  |
| 203 | `glPixelStorei` | `0x10310` | 84 | UnwindData |  |
| 110 | `glGetError` | `0x10370` | 64 | UnwindData |  |
| 82 | `glEnd` | `0x10660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `glBegin` | `0x10680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `glFrontFace` | `0x106A0` | 71 | UnwindData |  |
| 159 | `glLightfv` | `0x10C10` | 100 | UnwindData |  |
| 300 | `glTexEnvi` | `0x16290` | 100 | UnwindData |  |
| 5 | `GlmfInitPlayback` | `0x1CD10` | 426 | UnwindData |  |
| 343 | `glViewport` | `0x1CEC0` | 118 | UnwindData |  |
| 182 | `glMatrixMode` | `0x1CF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `glPushAttrib` | `0x1CF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `glPushMatrix` | `0x1CF80` | 1,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `glDrawElements` | `0x1D3F0` | 31 | UnwindData |  |
| 328 | `glVertex3f` | `0x1D420` | 8,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `glTexSubImage2D` | `0x1F600` | 175 | UnwindData |  |
| 275 | `glTexCoord2f` | `0x1F6C0` | 3,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `glColor4f` | `0x203D0` | 31 | UnwindData |  |
| 71 | `glDisable` | `0x20400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `glEnable` | `0x20420` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `glScissor` | `0x20A10` | 118 | UnwindData |  |
| 69 | `glDepthMask` | `0x20A90` | 73 | UnwindData |  |
| 14 | `glBlendFunc` | `0x212B0` | 84 | UnwindData |  |
| 12 | `glBindTexture` | `0x214E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `glTranslatef` | `0x21500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `glColorMask` | `0x21520` | 128 | UnwindData |  |
| 297 | `glTexCoordPointer` | `0x215B0` | 31 | UnwindData |  |
| 342 | `glVertexPointer` | `0x21EE0` | 31 | UnwindData |  |
| 213 | `glPopMatrix` | `0x22960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `glAlphaFunc` | `0x22980` | 87 | UnwindData |  |
| 256 | `glRotatef` | `0x229E0` | 31 | UnwindData |  |
| 81 | `glEnableClientState` | `0x23BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `glColorPointer` | `0x23C10` | 31 | UnwindData |  |
| 72 | `glDisableClientState` | `0x23C40` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `glNormal3f` | `0x243E0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `glGetFloatv` | `0x24520` | 86 | UnwindData |  |
| 155 | `glLightModelfv` | `0x24620` | 86 | UnwindData |  |
| 197 | `glOrtho` | `0x24680` | 174 | UnwindData |  |
| 68 | `glDepthFunc` | `0x247C0` | 71 | UnwindData |  |
| 73 | `glDrawArrays` | `0x24810` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `glClear` | `0x24E90` | 71 | UnwindData |  |
| 19 | `glClearColor` | `0x24EE0` | 138 | UnwindData |  |
| 100 | `glFogfv` | `0x24F70` | 86 | UnwindData |  |
| 15 | `glCallList` | `0x25AE0` | 2,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `wglGetCurrentContext` | `0x263F0` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `glShadeModel` | `0x26DC0` | 71 | UnwindData |  |
| 310 | `glTexParameterf` | `0x26E10` | 100 | UnwindData |  |
| 305 | `glTexGenfv` | `0x29430` | 100 | UnwindData |  |
| 329 | `glVertex3fv` | `0x29FD0` | 1,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `glScalef` | `0x2A720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `glTexParameteriv` | `0x2A740` | 100 | UnwindData |  |
| 327 | `glVertex3dv` | `0x2A7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `glMultMatrixf` | `0x2A7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `glIsEnabled` | `0x2A7F0` | 71 | UnwindData |  |
| 262 | `glStencilFunc` | `0x2A880` | 100 | UnwindData |  |
| 322 | `glVertex2i` | `0x2AA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `glLineWidth` | `0x2AA20` | 80 | UnwindData |  |
| 316 | `glTranslated` | `0x2AAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `glLoadIdentity` | `0x2AAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `glFlush` | `0x2AB00` | 64 | UnwindData |  |
| 263 | `glStencilMask` | `0x2AB50` | 71 | UnwindData |  |
| 196 | `glNormalPointer` | `0x2C8B0` | 3,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `glDepthRange` | `0x2D6B0` | 96 | UnwindData |  |
| 320 | `glVertex2f` | `0x2D720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `glClearDepth` | `0x2D740` | 80 | UnwindData |  |
| 64 | `glCullFace` | `0x2D7A0` | 71 | UnwindData |  |
| 298 | `glTexEnvf` | `0x2D7F0` | 100 | UnwindData |  |
| 264 | `glStencilOp` | `0x2D860` | 100 | UnwindData |  |
| 50 | `glColor4ub` | `0x2D8D0` | 31 | UnwindData |  |
| 99 | `glFogf` | `0x2D900` | 87 | UnwindData |  |
| 352 | `wglGetCurrentDC` | `0x2F190` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `glVertex2d` | `0x2F260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `glPolygonMode` | `0x2F280` | 84 | UnwindData |  |
| 57 | `glColorMaterial` | `0x2FC80` | 84 | UnwindData |  |
| 167 | `glLoadMatrixf` | `0x2FCE0` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `wglGetProcAddress` | `0x30400` | 190 | UnwindData |  |
| 107 | `glGetBooleanv` | `0x30800` | 86 | UnwindData |  |
| 135 | `glGetTexParameteriv` | `0x30BA0` | 100 | UnwindData |  |
| 101 | `glFogi` | `0x30E90` | 84 | UnwindData |  |
| 156 | `glLightModeli` | `0x30EF0` | 84 | UnwindData |  |
| 158 | `glLightf` | `0x311D0` | 100 | UnwindData |  |
| 133 | `glGetTexLevelParameteriv` | `0x31240` | 118 | UnwindData |  |
| 63 | `glCopyTexSubImage2D` | `0x314F0` | 162 | UnwindData |  |
| 309 | `glTexImage2D` | `0x31C90` | 175 | UnwindData |  |
| 22 | `glClearStencil` | `0x31DC0` | 71 | UnwindData |  |
| 228 | `glRasterPos3d` | `0x324E0` | 116 | UnwindData |  |
| 126 | `glGetTexEnvfv` | `0x32560` | 100 | UnwindData |  |
| 179 | `glMaterialfv` | `0x325D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `glPolygonOffset` | `0x325F0` | 11,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `glScaled` | `0x35340` | 5,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `glVertex3d` | `0x36850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `glHint` | `0x36870` | 84 | UnwindData |  |
| 244 | `glReadBuffer` | `0x368D0` | 71 | UnwindData |  |
| 164 | `glListBase` | `0x36A00` | 68 | UnwindData |  |
| 74 | `glDrawBuffer` | `0x36A50` | 71 | UnwindData |  |
| 106 | `glGenTextures` | `0x36AA0` | 86 | UnwindData |  |
| 127 | `glGetTexEnviv` | `0x37180` | 100 | UnwindData |  |
| 162 | `glLineStipple` | `0x371F0` | 86 | UnwindData |  |
| 66 | `glDeleteLists` | `0x37250` | 81 | UnwindData |  |
| 67 | `glDeleteTextures` | `0x373F0` | 86 | UnwindData |  |
| 207 | `glPointSize` | `0x374C0` | 80 | UnwindData |  |
| 105 | `glGenLists` | `0x37520` | 68 | UnwindData |  |
| 45 | `glColor4fv` | `0x38140` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `glGetDoublev` | `0x38420` | 86 | UnwindData |  |
| 273 | `glTexCoord2d` | `0x388B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `glReadPixels` | `0x388D0` | 147 | UnwindData |  |
| 153 | `glIsTexture` | `0x393D0` | 71 | UnwindData |  |
| 28 | `glColor3f` | `0x39AD0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `glLoadName` | `0x39BC0` | 71 | UnwindData |  |
| 178 | `glMaterialf` | `0x39F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `glNormal3dv` | `0x39F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `glDrawPixels` | `0x39FA0` | 128 | UnwindData |  |
| 299 | `glTexEnvfv` | `0x3A0B0` | 100 | UnwindData |  |
| 125 | `glGetString` | `0x3A120` | 71 | UnwindData |  |
| 152 | `glIsList` | `0x3A260` | 71 | UnwindData |  |
| 211 | `glPopAttrib` | `0x3A6D0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `glTexParameterfv` | `0x3A960` | 100 | UnwindData |  |
| 188 | `glNormal3d` | `0x3A9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `glCallLists` | `0x3A9F0` | 1,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `glGetLightfv` | `0x3B120` | 100 | UnwindData |  |
| 265 | `glTexCoord1d` | `0x3B190` | 2,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `glRotated` | `0x3BA50` | 31 | UnwindData |  |
| 51 | `glColor4ubv` | `0x3BBE0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `glLoadMatrixd` | `0x3BF40` | 5,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `glLogicOp` | `0x3D320` | 71 | UnwindData |  |
| 230 | `glRasterPos3f` | `0x3D370` | 116 | UnwindData |  |
| 248 | `glRectf` | `0x3E120` | 137 | UnwindData |  |
| 134 | `glGetTexParameterfv` | `0x3E1B0` | 100 | UnwindData |  |
| 321 | `glVertex2fv` | `0x3E220` | 2,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `glCopyTexImage2D` | `0x3ED90` | 162 | UnwindData |  |
| 23 | `glClipPlane` | `0x3F020` | 86 | UnwindData |  |
| 254 | `glRenderMode` | `0x3F370` | 71 | UnwindData |  |
| 42 | `glColor4d` | `0x3F3C0` | 31 | UnwindData |  |
| 222 | `glRasterPos2f` | `0x403C0` | 96 | UnwindData |  |
| 212 | `glPopClientAttrib` | `0x40530` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `glPushClientAttrib` | `0x405B0` | 3,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `glMap1f` | `0x411B0` | 144 | UnwindData |  |
| 219 | `glPushName` | `0x41250` | 71 | UnwindData |  |
| 29 | `glColor3fv` | `0x416E0` | 1,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `glPixelZoom` | `0x41DD0` | 96 | UnwindData |  |
| 183 | `glMultMatrixd` | `0x42640` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `glColor3ubv` | `0x426D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `glSelectBuffer` | `0x42760` | 86 | UnwindData |  |
| 34 | `glColor3ub` | `0x438B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `glFrustum` | `0x43910` | 173 | UnwindData |  |
| 204 | `glPixelTransferf` | `0x43CA0` | 87 | UnwindData |  |
| 276 | `glTexCoord2fv` | `0x43E00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `glArrayElement` | `0x43F30` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `glTexImage1D` | `0x44080` | 164 | UnwindData |  |
| 224 | `glRasterPos2i` | `0x44DA0` | 84 | UnwindData |  |
| 149 | `glInitNames` | `0x44E00` | 64 | UnwindData |  |
| 238 | `glRasterPos4f` | `0x451A0` | 137 | UnwindData |  |
| 205 | `glPixelTransferi` | `0x45790` | 84 | UnwindData |  |
| 172 | `glMap2d` | `0x45900` | 208 | UnwindData |  |
| 131 | `glGetTexImage` | `0x45C00` | 128 | UnwindData |  |
| 314 | `glTexSubImage1D` | `0x46400` | 147 | UnwindData |  |
| 267 | `glTexCoord1f` | `0x46520` | 3,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `glTexCoord2i` | `0x474A0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `glTexGeni` | `0x47530` | 100 | UnwindData |  |
| 160 | `glLighti` | `0x475A0` | 100 | UnwindData |  |
| 210 | `glPolygonStipple` | `0x48CF0` | 73 | UnwindData |  |
| 214 | `glPopName` | `0x48E90` | 64 | UnwindData |  |
| 229 | `glRasterPos3dv` | `0x48EE0` | 73 | UnwindData |  |
| 65 | `glDebugEntry` | `0x4B540` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `glEdgeFlag` | `0x4C180` | 6,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `glInterleavedArrays` | `0x4DC50` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `glVertex2s` | `0x4E120` | 2,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `glVertex4f` | `0x4EB90` | 31 | UnwindData |  |
| 180 | `glMateriali` | `0x4F3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `glTexCoord3f` | `0x4F3F0` | 3,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `wglCreateContext` | `0x50130` | 4,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `glTexCoord4f` | `0x514B0` | 31 | UnwindData |  |
| 354 | `wglGetLayerPaletteEntries` | `0x519A0` | 171 | UnwindData |  |
| 274 | `glTexCoord2dv` | `0x53330` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `glRasterPos4i` | `0x534B0` | 118 | UnwindData |  |
| 154 | `glLightModelf` | `0x53750` | 87 | UnwindData |  |
| 232 | `glRasterPos3i` | `0x537B0` | 100 | UnwindData |  |
| 303 | `glTexGendv` | `0x53820` | 100 | UnwindData |  |
| 92 | `glEvalMesh1` | `0x53890` | 100 | UnwindData |  |
| 175 | `glMapGrid1f` | `0x53900` | 103 | UnwindData |  |
| 366 | `wglUseFontBitmapsW` | `0x55A40` | 23 | UnwindData |  |
| 26 | `glColor3d` | `0x58120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `glVertex2dv` | `0x58140` | 6,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `glTexCoord4d` | `0x59AF0` | 31 | UnwindData |  |
| 367 | `wglUseFontOutlinesA` | `0x61DE0` | 74 | UnwindData |  |
| 368 | `wglUseFontOutlinesW` | `0x61E30` | 77 | UnwindData |  |
| 349 | `wglDescribeLayerPlane` | `0x6BAA0` | 201 | UnwindData |  |
| 358 | `wglRealizeLayerPalette` | `0x6BB70` | 176 | UnwindData |  |
| 359 | `wglSetLayerPaletteEntries` | `0x6BC30` | 194 | UnwindData |  |
| 1 | `GlmfBeginGlsBlock` | `0x6BEA0` | 91 | UnwindData |  |
| 2 | `GlmfCloseMetaFile` | `0x6BF10` | 161 | UnwindData |  |
| 3 | `GlmfEndGlsBlock` | `0x6BFC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GlmfEndPlayback` | `0x6C000` | 119 | UnwindData |  |
| 6 | `GlmfPlayGlsRecord` | `0x6C080` | 395 | UnwindData |  |
| 364 | `wglSwapMultipleBuffers` | `0x6CB60` | 1,194 | UnwindData |  |
| 345 | `wglCopyContext` | `0x6DE30` | 298 | UnwindData |  |
| 353 | `wglGetDefaultProcAddress` | `0x6DF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `wglUseFontBitmapsA` | `0x6DF70` | 20 | UnwindData |  |
| 7 | `glAccum` | `0x6E430` | 87 | UnwindData |  |
| 9 | `glAreTexturesResident` | `0x6E490` | 102 | UnwindData |  |
| 18 | `glClearAccum` | `0x6E500` | 137 | UnwindData |  |
| 21 | `glClearIndex` | `0x6E590` | 80 | UnwindData |  |
| 24 | `glColor3b` | `0x6E5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `glColor3bv` | `0x6E610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `glColor3dv` | `0x6E630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `glColor3i` | `0x6E650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `glColor3iv` | `0x6E670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `glColor3s` | `0x6E690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `glColor3sv` | `0x6E6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `glColor3ui` | `0x6E6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `glColor3uiv` | `0x6E6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `glColor3us` | `0x6E710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `glColor3usv` | `0x6E730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `glColor4b` | `0x6E750` | 31 | UnwindData |  |
| 41 | `glColor4bv` | `0x6E780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `glColor4dv` | `0x6E7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `glColor4i` | `0x6E7C0` | 31 | UnwindData |  |
| 47 | `glColor4iv` | `0x6E7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `glColor4s` | `0x6E810` | 31 | UnwindData |  |
| 49 | `glColor4sv` | `0x6E840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `glColor4ui` | `0x6E860` | 31 | UnwindData |  |
| 53 | `glColor4uiv` | `0x6E890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `glColor4us` | `0x6E8B0` | 31 | UnwindData |  |
| 55 | `glColor4usv` | `0x6E8E0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `glCopyPixels` | `0x6E980` | 126 | UnwindData |  |
| 60 | `glCopyTexImage1D` | `0x6EA10` | 145 | UnwindData |  |
| 62 | `glCopyTexSubImage1D` | `0x6EAB0` | 134 | UnwindData |  |
| 78 | `glEdgeFlagPointer` | `0x6EB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `glEdgeFlagv` | `0x6EBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `glEvalCoord1d` | `0x6EBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `glEvalCoord1dv` | `0x6EBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `glEvalCoord1f` | `0x6EC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `glEvalCoord1fv` | `0x6EC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `glEvalCoord2d` | `0x6EC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `glEvalCoord2dv` | `0x6EC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `glEvalCoord2f` | `0x6EC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `glEvalCoord2fv` | `0x6ECA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `glEvalMesh2` | `0x6ECC0` | 126 | UnwindData |  |
| 94 | `glEvalPoint1` | `0x6ED50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `glEvalPoint2` | `0x6ED70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `glFeedbackBuffer` | `0x6ED90` | 100 | UnwindData |  |
| 102 | `glFogiv` | `0x6EE00` | 86 | UnwindData |  |
| 108 | `glGetClipPlane` | `0x6EE60` | 86 | UnwindData |  |
| 114 | `glGetLightiv` | `0x6F020` | 100 | UnwindData |  |
| 115 | `glGetMapdv` | `0x6F090` | 100 | UnwindData |  |
| 116 | `glGetMapfv` | `0x6F100` | 100 | UnwindData |  |
| 117 | `glGetMapiv` | `0x6F170` | 100 | UnwindData |  |
| 118 | `glGetMaterialfv` | `0x6F1E0` | 100 | UnwindData |  |
| 119 | `glGetMaterialiv` | `0x6F250` | 100 | UnwindData |  |
| 120 | `glGetPixelMapfv` | `0x6F2C0` | 86 | UnwindData |  |
| 121 | `glGetPixelMapuiv` | `0x6F320` | 86 | UnwindData |  |
| 122 | `glGetPixelMapusv` | `0x6F380` | 86 | UnwindData |  |
| 123 | `glGetPointerv` | `0x6F3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `glGetPolygonStipple` | `0x6F400` | 73 | UnwindData |  |
| 128 | `glGetTexGendv` | `0x6F450` | 100 | UnwindData |  |
| 129 | `glGetTexGenfv` | `0x6F4C0` | 100 | UnwindData |  |
| 130 | `glGetTexGeniv` | `0x6F530` | 100 | UnwindData |  |
| 132 | `glGetTexLevelParameterfv` | `0x6F5A0` | 118 | UnwindData |  |
| 137 | `glIndexMask` | `0x6F620` | 71 | UnwindData |  |
| 138 | `glIndexPointer` | `0x6F670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `glIndexd` | `0x6F690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `glIndexdv` | `0x6F6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `glIndexf` | `0x6F6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `glIndexfv` | `0x6F6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `glIndexi` | `0x6F710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `glIndexiv` | `0x6F730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `glIndexs` | `0x6F750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `glIndexsv` | `0x6F770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `glIndexub` | `0x6F790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `glIndexubv` | `0x6F7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `glLightModeliv` | `0x6F7D0` | 86 | UnwindData |  |
| 161 | `glLightiv` | `0x6F830` | 100 | UnwindData |  |
| 170 | `glMap1d` | `0x6F8A0` | 144 | UnwindData |  |
| 173 | `glMap2f` | `0x6F940` | 208 | UnwindData |  |
| 174 | `glMapGrid1d` | `0x6FA20` | 103 | UnwindData |  |
| 176 | `glMapGrid2d` | `0x6FA90` | 150 | UnwindData |  |
| 177 | `glMapGrid2f` | `0x6FB30` | 150 | UnwindData |  |
| 181 | `glMaterialiv` | `0x6FBD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `glNormal3b` | `0x6FBF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `glNormal3bv` | `0x6FC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `glNormal3i` | `0x6FC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `glNormal3iv` | `0x6FC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `glNormal3s` | `0x6FC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `glNormal3sv` | `0x6FC90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `glPassThrough` | `0x6FCB0` | 80 | UnwindData |  |
| 199 | `glPixelMapfv` | `0x6FD10` | 100 | UnwindData |  |
| 200 | `glPixelMapuiv` | `0x6FD80` | 100 | UnwindData |  |
| 201 | `glPixelMapusv` | `0x6FDF0` | 100 | UnwindData |  |
| 202 | `glPixelStoref` | `0x6FE60` | 87 | UnwindData |  |
| 215 | `glPrioritizeTextures` | `0x6FEC0` | 102 | UnwindData |  |
| 220 | `glRasterPos2d` | `0x6FF30` | 96 | UnwindData |  |
| 221 | `glRasterPos2dv` | `0x6FFA0` | 73 | UnwindData |  |
| 223 | `glRasterPos2fv` | `0x6FFF0` | 73 | UnwindData |  |
| 225 | `glRasterPos2iv` | `0x70040` | 73 | UnwindData |  |
| 226 | `glRasterPos2s` | `0x70090` | 88 | UnwindData |  |
| 227 | `glRasterPos2sv` | `0x700F0` | 73 | UnwindData |  |
| 231 | `glRasterPos3fv` | `0x70140` | 73 | UnwindData |  |
| 233 | `glRasterPos3iv` | `0x70190` | 73 | UnwindData |  |
| 234 | `glRasterPos3s` | `0x701E0` | 106 | UnwindData |  |
| 235 | `glRasterPos3sv` | `0x70250` | 73 | UnwindData |  |
| 236 | `glRasterPos4d` | `0x702A0` | 137 | UnwindData |  |
| 237 | `glRasterPos4dv` | `0x70330` | 73 | UnwindData |  |
| 239 | `glRasterPos4fv` | `0x70380` | 73 | UnwindData |  |
| 241 | `glRasterPos4iv` | `0x703D0` | 73 | UnwindData |  |
| 242 | `glRasterPos4s` | `0x70420` | 126 | UnwindData |  |
| 243 | `glRasterPos4sv` | `0x704B0` | 73 | UnwindData |  |
| 246 | `glRectd` | `0x70500` | 137 | UnwindData |  |
| 247 | `glRectdv` | `0x70590` | 88 | UnwindData |  |
| 249 | `glRectfv` | `0x705F0` | 88 | UnwindData |  |
| 250 | `glRecti` | `0x70650` | 118 | UnwindData |  |
| 251 | `glRectiv` | `0x706D0` | 88 | UnwindData |  |
| 252 | `glRects` | `0x70730` | 126 | UnwindData |  |
| 253 | `glRectsv` | `0x707C0` | 88 | UnwindData |  |
| 266 | `glTexCoord1dv` | `0x70820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `glTexCoord1fv` | `0x70840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `glTexCoord1i` | `0x70860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `glTexCoord1iv` | `0x70880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `glTexCoord1s` | `0x708A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `glTexCoord1sv` | `0x708C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `glTexCoord2iv` | `0x708E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `glTexCoord2s` | `0x70900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `glTexCoord2sv` | `0x70920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `glTexCoord3d` | `0x70940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `glTexCoord3dv` | `0x70960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `glTexCoord3fv` | `0x70980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `glTexCoord3i` | `0x709A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `glTexCoord3iv` | `0x709C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `glTexCoord3s` | `0x709E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `glTexCoord3sv` | `0x70A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `glTexCoord4dv` | `0x70A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `glTexCoord4fv` | `0x70A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `glTexCoord4i` | `0x70A60` | 31 | UnwindData |  |
| 294 | `glTexCoord4iv` | `0x70A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `glTexCoord4s` | `0x70AB0` | 31 | UnwindData |  |
| 296 | `glTexCoord4sv` | `0x70AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `glTexEnviv` | `0x70B00` | 100 | UnwindData |  |
| 302 | `glTexGend` | `0x70B70` | 100 | UnwindData |  |
| 304 | `glTexGenf` | `0x70BE0` | 100 | UnwindData |  |
| 307 | `glTexGeniv` | `0x70C50` | 100 | UnwindData |  |
| 323 | `glVertex2iv` | `0x70CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `glVertex2sv` | `0x70CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `glVertex3i` | `0x70D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `glVertex3iv` | `0x70D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `glVertex3s` | `0x70D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `glVertex3sv` | `0x70D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `glVertex4d` | `0x70D80` | 31 | UnwindData |  |
| 335 | `glVertex4dv` | `0x70DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `glVertex4fv` | `0x70DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `glVertex4i` | `0x70DF0` | 31 | UnwindData |  |
| 339 | `glVertex4iv` | `0x70E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `glVertex4s` | `0x70E40` | 31 | UnwindData |  |
| 341 | `glVertex4sv` | `0x70E70` | 361,996 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
