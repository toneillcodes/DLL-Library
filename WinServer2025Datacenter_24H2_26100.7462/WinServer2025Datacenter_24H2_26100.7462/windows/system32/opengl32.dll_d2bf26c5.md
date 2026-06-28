# Binary Specification: opengl32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\opengl32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d2bf26c571a75ce4cbf0cc95f1f87993a44cbc434ad80b918333710177559c5a`
* **Total Exported Functions:** 368

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 348 | `wglDeleteContext` | `0x4C20` | 202 | UnwindData |  |
| 361 | `wglShareLists` | `0x4E40` | 518 | UnwindData |  |
| 357 | `wglMakeCurrent` | `0x5050` | 105 | UnwindData |  |
| 347 | `wglCreateLayerContext` | `0x6170` | 591 | UnwindData |  |
| 344 | `wglChoosePixelFormat` | `0x6720` | 1,582 | UnwindData |  |
| 350 | `wglDescribePixelFormat` | `0x6DC0` | 142 | UnwindData |  |
| 362 | `wglSwapBuffers` | `0x7F70` | 100 | UnwindData |  |
| 355 | `wglGetPixelFormat` | `0x84E0` | 296 | UnwindData |  |
| 97 | `glFinish` | `0x8690` | 64 | UnwindData |  |
| 360 | `wglSetPixelFormat` | `0x86E0` | 922 | UnwindData |  |
| 363 | `wglSwapLayerBuffers` | `0xAB50` | 328 | UnwindData |  |
| 312 | `glTexParameteri` | `0xDEF0` | 100 | UnwindData |  |
| 191 | `glNormal3fv` | `0xE9A0` | 6,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `glBitmap` | `0x10140` | 158 | UnwindData |  |
| 83 | `glEndList` | `0x101F0` | 61 | UnwindData |  |
| 185 | `glNewList` | `0x10240` | 80 | UnwindData |  |
| 112 | `glGetIntegerv` | `0x102A0` | 86 | UnwindData |  |
| 203 | `glPixelStorei` | `0x10300` | 84 | UnwindData |  |
| 110 | `glGetError` | `0x10360` | 64 | UnwindData |  |
| 82 | `glEnd` | `0x10650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `glBegin` | `0x10670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `glFrontFace` | `0x10690` | 71 | UnwindData |  |
| 159 | `glLightfv` | `0x10C00` | 100 | UnwindData |  |
| 300 | `glTexEnvi` | `0x16280` | 100 | UnwindData |  |
| 5 | `GlmfInitPlayback` | `0x1CD00` | 426 | UnwindData |  |
| 343 | `glViewport` | `0x1CEB0` | 118 | UnwindData |  |
| 182 | `glMatrixMode` | `0x1CF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `glPushAttrib` | `0x1CF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `glPushMatrix` | `0x1CF70` | 1,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `glDrawElements` | `0x1D3E0` | 31 | UnwindData |  |
| 328 | `glVertex3f` | `0x1D410` | 8,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `glTexSubImage2D` | `0x1F5F0` | 175 | UnwindData |  |
| 275 | `glTexCoord2f` | `0x1F6B0` | 3,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `glColor4f` | `0x203C0` | 31 | UnwindData |  |
| 71 | `glDisable` | `0x203F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `glEnable` | `0x20410` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `glScissor` | `0x20A00` | 118 | UnwindData |  |
| 69 | `glDepthMask` | `0x20A80` | 73 | UnwindData |  |
| 14 | `glBlendFunc` | `0x212A0` | 84 | UnwindData |  |
| 12 | `glBindTexture` | `0x214D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `glTranslatef` | `0x214F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `glColorMask` | `0x21510` | 128 | UnwindData |  |
| 297 | `glTexCoordPointer` | `0x215A0` | 31 | UnwindData |  |
| 342 | `glVertexPointer` | `0x21ED0` | 31 | UnwindData |  |
| 213 | `glPopMatrix` | `0x22950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `glAlphaFunc` | `0x22970` | 87 | UnwindData |  |
| 256 | `glRotatef` | `0x229D0` | 31 | UnwindData |  |
| 81 | `glEnableClientState` | `0x23BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `glColorPointer` | `0x23C00` | 31 | UnwindData |  |
| 72 | `glDisableClientState` | `0x23C30` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `glNormal3f` | `0x243D0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `glGetFloatv` | `0x24510` | 86 | UnwindData |  |
| 155 | `glLightModelfv` | `0x24610` | 86 | UnwindData |  |
| 197 | `glOrtho` | `0x24670` | 174 | UnwindData |  |
| 68 | `glDepthFunc` | `0x247B0` | 71 | UnwindData |  |
| 73 | `glDrawArrays` | `0x24800` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `glClear` | `0x24E80` | 71 | UnwindData |  |
| 19 | `glClearColor` | `0x24ED0` | 138 | UnwindData |  |
| 100 | `glFogfv` | `0x24F60` | 86 | UnwindData |  |
| 15 | `glCallList` | `0x25AD0` | 2,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `wglGetCurrentContext` | `0x263E0` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `glShadeModel` | `0x26DB0` | 71 | UnwindData |  |
| 310 | `glTexParameterf` | `0x26E00` | 100 | UnwindData |  |
| 305 | `glTexGenfv` | `0x29420` | 100 | UnwindData |  |
| 329 | `glVertex3fv` | `0x29FC0` | 1,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `glScalef` | `0x2A710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `glTexParameteriv` | `0x2A730` | 100 | UnwindData |  |
| 327 | `glVertex3dv` | `0x2A7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `glMultMatrixf` | `0x2A7C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `glIsEnabled` | `0x2A7E0` | 71 | UnwindData |  |
| 262 | `glStencilFunc` | `0x2A870` | 100 | UnwindData |  |
| 322 | `glVertex2i` | `0x2A9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `glLineWidth` | `0x2AA10` | 80 | UnwindData |  |
| 316 | `glTranslated` | `0x2AAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `glLoadIdentity` | `0x2AAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `glFlush` | `0x2AAF0` | 64 | UnwindData |  |
| 263 | `glStencilMask` | `0x2AB40` | 71 | UnwindData |  |
| 196 | `glNormalPointer` | `0x2C8A0` | 3,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `glDepthRange` | `0x2D6A0` | 96 | UnwindData |  |
| 320 | `glVertex2f` | `0x2D710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `glClearDepth` | `0x2D730` | 80 | UnwindData |  |
| 64 | `glCullFace` | `0x2D790` | 71 | UnwindData |  |
| 298 | `glTexEnvf` | `0x2D7E0` | 100 | UnwindData |  |
| 264 | `glStencilOp` | `0x2D850` | 100 | UnwindData |  |
| 50 | `glColor4ub` | `0x2D8C0` | 31 | UnwindData |  |
| 99 | `glFogf` | `0x2D8F0` | 87 | UnwindData |  |
| 352 | `wglGetCurrentDC` | `0x2F180` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `glVertex2d` | `0x2F250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `glPolygonMode` | `0x2F270` | 84 | UnwindData |  |
| 57 | `glColorMaterial` | `0x2FC70` | 84 | UnwindData |  |
| 167 | `glLoadMatrixf` | `0x2FCD0` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `wglGetProcAddress` | `0x303F0` | 190 | UnwindData |  |
| 107 | `glGetBooleanv` | `0x307F0` | 86 | UnwindData |  |
| 135 | `glGetTexParameteriv` | `0x30B90` | 100 | UnwindData |  |
| 101 | `glFogi` | `0x30E80` | 84 | UnwindData |  |
| 156 | `glLightModeli` | `0x30EE0` | 84 | UnwindData |  |
| 158 | `glLightf` | `0x311C0` | 100 | UnwindData |  |
| 133 | `glGetTexLevelParameteriv` | `0x31230` | 118 | UnwindData |  |
| 63 | `glCopyTexSubImage2D` | `0x314E0` | 162 | UnwindData |  |
| 309 | `glTexImage2D` | `0x31C80` | 175 | UnwindData |  |
| 22 | `glClearStencil` | `0x31DB0` | 71 | UnwindData |  |
| 228 | `glRasterPos3d` | `0x324D0` | 116 | UnwindData |  |
| 126 | `glGetTexEnvfv` | `0x32550` | 100 | UnwindData |  |
| 179 | `glMaterialfv` | `0x325C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `glPolygonOffset` | `0x325E0` | 11,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `glScaled` | `0x35330` | 5,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `glVertex3d` | `0x36840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `glHint` | `0x36860` | 84 | UnwindData |  |
| 244 | `glReadBuffer` | `0x368C0` | 71 | UnwindData |  |
| 164 | `glListBase` | `0x369F0` | 68 | UnwindData |  |
| 74 | `glDrawBuffer` | `0x36A40` | 71 | UnwindData |  |
| 106 | `glGenTextures` | `0x36A90` | 86 | UnwindData |  |
| 127 | `glGetTexEnviv` | `0x37170` | 100 | UnwindData |  |
| 162 | `glLineStipple` | `0x371E0` | 86 | UnwindData |  |
| 66 | `glDeleteLists` | `0x37240` | 81 | UnwindData |  |
| 67 | `glDeleteTextures` | `0x373E0` | 86 | UnwindData |  |
| 207 | `glPointSize` | `0x374B0` | 80 | UnwindData |  |
| 105 | `glGenLists` | `0x37510` | 68 | UnwindData |  |
| 45 | `glColor4fv` | `0x38130` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `glGetDoublev` | `0x38410` | 86 | UnwindData |  |
| 273 | `glTexCoord2d` | `0x388A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `glReadPixels` | `0x388C0` | 147 | UnwindData |  |
| 153 | `glIsTexture` | `0x393C0` | 71 | UnwindData |  |
| 28 | `glColor3f` | `0x39AC0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `glLoadName` | `0x39BB0` | 71 | UnwindData |  |
| 178 | `glMaterialf` | `0x39F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `glNormal3dv` | `0x39F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `glDrawPixels` | `0x39F90` | 128 | UnwindData |  |
| 299 | `glTexEnvfv` | `0x3A0A0` | 100 | UnwindData |  |
| 125 | `glGetString` | `0x3A110` | 71 | UnwindData |  |
| 152 | `glIsList` | `0x3A250` | 71 | UnwindData |  |
| 211 | `glPopAttrib` | `0x3A6C0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `glTexParameterfv` | `0x3A950` | 100 | UnwindData |  |
| 188 | `glNormal3d` | `0x3A9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `glCallLists` | `0x3A9E0` | 1,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `glGetLightfv` | `0x3B110` | 100 | UnwindData |  |
| 265 | `glTexCoord1d` | `0x3B180` | 2,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `glRotated` | `0x3BA40` | 31 | UnwindData |  |
| 51 | `glColor4ubv` | `0x3BBD0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `glLoadMatrixd` | `0x3BF30` | 5,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `glLogicOp` | `0x3D310` | 71 | UnwindData |  |
| 230 | `glRasterPos3f` | `0x3D360` | 116 | UnwindData |  |
| 248 | `glRectf` | `0x3E110` | 137 | UnwindData |  |
| 134 | `glGetTexParameterfv` | `0x3E1A0` | 100 | UnwindData |  |
| 321 | `glVertex2fv` | `0x3E210` | 2,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `glCopyTexImage2D` | `0x3ED80` | 162 | UnwindData |  |
| 23 | `glClipPlane` | `0x3F010` | 86 | UnwindData |  |
| 254 | `glRenderMode` | `0x3F360` | 71 | UnwindData |  |
| 42 | `glColor4d` | `0x3F3B0` | 31 | UnwindData |  |
| 222 | `glRasterPos2f` | `0x403B0` | 96 | UnwindData |  |
| 212 | `glPopClientAttrib` | `0x40520` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `glPushClientAttrib` | `0x405A0` | 3,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `glMap1f` | `0x411A0` | 144 | UnwindData |  |
| 219 | `glPushName` | `0x41240` | 71 | UnwindData |  |
| 29 | `glColor3fv` | `0x416D0` | 1,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `glPixelZoom` | `0x41DC0` | 96 | UnwindData |  |
| 183 | `glMultMatrixd` | `0x42630` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `glColor3ubv` | `0x426C0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `glSelectBuffer` | `0x42750` | 86 | UnwindData |  |
| 34 | `glColor3ub` | `0x438A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `glFrustum` | `0x43900` | 173 | UnwindData |  |
| 204 | `glPixelTransferf` | `0x43C90` | 87 | UnwindData |  |
| 276 | `glTexCoord2fv` | `0x43DF0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `glArrayElement` | `0x43F20` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `glTexImage1D` | `0x44070` | 164 | UnwindData |  |
| 224 | `glRasterPos2i` | `0x44D90` | 84 | UnwindData |  |
| 149 | `glInitNames` | `0x44DF0` | 64 | UnwindData |  |
| 238 | `glRasterPos4f` | `0x45190` | 137 | UnwindData |  |
| 205 | `glPixelTransferi` | `0x45780` | 84 | UnwindData |  |
| 172 | `glMap2d` | `0x458F0` | 208 | UnwindData |  |
| 131 | `glGetTexImage` | `0x45BF0` | 128 | UnwindData |  |
| 314 | `glTexSubImage1D` | `0x463F0` | 147 | UnwindData |  |
| 267 | `glTexCoord1f` | `0x46510` | 3,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `glTexCoord2i` | `0x47490` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `glTexGeni` | `0x47520` | 100 | UnwindData |  |
| 160 | `glLighti` | `0x47590` | 100 | UnwindData |  |
| 210 | `glPolygonStipple` | `0x48CE0` | 73 | UnwindData |  |
| 214 | `glPopName` | `0x48E80` | 64 | UnwindData |  |
| 229 | `glRasterPos3dv` | `0x48ED0` | 73 | UnwindData |  |
| 65 | `glDebugEntry` | `0x4B530` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `glEdgeFlag` | `0x4C170` | 6,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `glInterleavedArrays` | `0x4DC40` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `glVertex2s` | `0x4E110` | 2,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `glVertex4f` | `0x4EB80` | 31 | UnwindData |  |
| 180 | `glMateriali` | `0x4F3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `glTexCoord3f` | `0x4F3E0` | 3,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `wglCreateContext` | `0x50120` | 4,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `glTexCoord4f` | `0x514A0` | 31 | UnwindData |  |
| 354 | `wglGetLayerPaletteEntries` | `0x51990` | 171 | UnwindData |  |
| 274 | `glTexCoord2dv` | `0x53320` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `glRasterPos4i` | `0x534A0` | 118 | UnwindData |  |
| 154 | `glLightModelf` | `0x53740` | 87 | UnwindData |  |
| 232 | `glRasterPos3i` | `0x537A0` | 100 | UnwindData |  |
| 303 | `glTexGendv` | `0x53810` | 100 | UnwindData |  |
| 92 | `glEvalMesh1` | `0x53880` | 100 | UnwindData |  |
| 175 | `glMapGrid1f` | `0x538F0` | 103 | UnwindData |  |
| 366 | `wglUseFontBitmapsW` | `0x55A30` | 23 | UnwindData |  |
| 26 | `glColor3d` | `0x58110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `glVertex2dv` | `0x58130` | 6,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `glTexCoord4d` | `0x59AE0` | 31 | UnwindData |  |
| 367 | `wglUseFontOutlinesA` | `0x61DD0` | 74 | UnwindData |  |
| 368 | `wglUseFontOutlinesW` | `0x61E20` | 77 | UnwindData |  |
| 349 | `wglDescribeLayerPlane` | `0x6BA90` | 201 | UnwindData |  |
| 358 | `wglRealizeLayerPalette` | `0x6BB60` | 176 | UnwindData |  |
| 359 | `wglSetLayerPaletteEntries` | `0x6BC20` | 194 | UnwindData |  |
| 1 | `GlmfBeginGlsBlock` | `0x6BE90` | 91 | UnwindData |  |
| 2 | `GlmfCloseMetaFile` | `0x6BF00` | 161 | UnwindData |  |
| 3 | `GlmfEndGlsBlock` | `0x6BFB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GlmfEndPlayback` | `0x6BFF0` | 119 | UnwindData |  |
| 6 | `GlmfPlayGlsRecord` | `0x6C070` | 395 | UnwindData |  |
| 364 | `wglSwapMultipleBuffers` | `0x6CB50` | 1,194 | UnwindData |  |
| 345 | `wglCopyContext` | `0x6DE20` | 298 | UnwindData |  |
| 353 | `wglGetDefaultProcAddress` | `0x6DF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `wglUseFontBitmapsA` | `0x6DF60` | 20 | UnwindData |  |
| 7 | `glAccum` | `0x6E420` | 87 | UnwindData |  |
| 9 | `glAreTexturesResident` | `0x6E480` | 102 | UnwindData |  |
| 18 | `glClearAccum` | `0x6E4F0` | 137 | UnwindData |  |
| 21 | `glClearIndex` | `0x6E580` | 80 | UnwindData |  |
| 24 | `glColor3b` | `0x6E5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `glColor3bv` | `0x6E600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `glColor3dv` | `0x6E620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `glColor3i` | `0x6E640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `glColor3iv` | `0x6E660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `glColor3s` | `0x6E680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `glColor3sv` | `0x6E6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `glColor3ui` | `0x6E6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `glColor3uiv` | `0x6E6E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `glColor3us` | `0x6E700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `glColor3usv` | `0x6E720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `glColor4b` | `0x6E740` | 31 | UnwindData |  |
| 41 | `glColor4bv` | `0x6E770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `glColor4dv` | `0x6E790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `glColor4i` | `0x6E7B0` | 31 | UnwindData |  |
| 47 | `glColor4iv` | `0x6E7E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `glColor4s` | `0x6E800` | 31 | UnwindData |  |
| 49 | `glColor4sv` | `0x6E830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `glColor4ui` | `0x6E850` | 31 | UnwindData |  |
| 53 | `glColor4uiv` | `0x6E880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `glColor4us` | `0x6E8A0` | 31 | UnwindData |  |
| 55 | `glColor4usv` | `0x6E8D0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `glCopyPixels` | `0x6E970` | 126 | UnwindData |  |
| 60 | `glCopyTexImage1D` | `0x6EA00` | 145 | UnwindData |  |
| 62 | `glCopyTexSubImage1D` | `0x6EAA0` | 134 | UnwindData |  |
| 78 | `glEdgeFlagPointer` | `0x6EB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `glEdgeFlagv` | `0x6EB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `glEvalCoord1d` | `0x6EBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `glEvalCoord1dv` | `0x6EBD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `glEvalCoord1f` | `0x6EBF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `glEvalCoord1fv` | `0x6EC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `glEvalCoord2d` | `0x6EC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `glEvalCoord2dv` | `0x6EC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `glEvalCoord2f` | `0x6EC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `glEvalCoord2fv` | `0x6EC90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `glEvalMesh2` | `0x6ECB0` | 126 | UnwindData |  |
| 94 | `glEvalPoint1` | `0x6ED40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `glEvalPoint2` | `0x6ED60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `glFeedbackBuffer` | `0x6ED80` | 100 | UnwindData |  |
| 102 | `glFogiv` | `0x6EDF0` | 86 | UnwindData |  |
| 108 | `glGetClipPlane` | `0x6EE50` | 86 | UnwindData |  |
| 114 | `glGetLightiv` | `0x6F010` | 100 | UnwindData |  |
| 115 | `glGetMapdv` | `0x6F080` | 100 | UnwindData |  |
| 116 | `glGetMapfv` | `0x6F0F0` | 100 | UnwindData |  |
| 117 | `glGetMapiv` | `0x6F160` | 100 | UnwindData |  |
| 118 | `glGetMaterialfv` | `0x6F1D0` | 100 | UnwindData |  |
| 119 | `glGetMaterialiv` | `0x6F240` | 100 | UnwindData |  |
| 120 | `glGetPixelMapfv` | `0x6F2B0` | 86 | UnwindData |  |
| 121 | `glGetPixelMapuiv` | `0x6F310` | 86 | UnwindData |  |
| 122 | `glGetPixelMapusv` | `0x6F370` | 86 | UnwindData |  |
| 123 | `glGetPointerv` | `0x6F3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `glGetPolygonStipple` | `0x6F3F0` | 73 | UnwindData |  |
| 128 | `glGetTexGendv` | `0x6F440` | 100 | UnwindData |  |
| 129 | `glGetTexGenfv` | `0x6F4B0` | 100 | UnwindData |  |
| 130 | `glGetTexGeniv` | `0x6F520` | 100 | UnwindData |  |
| 132 | `glGetTexLevelParameterfv` | `0x6F590` | 118 | UnwindData |  |
| 137 | `glIndexMask` | `0x6F610` | 71 | UnwindData |  |
| 138 | `glIndexPointer` | `0x6F660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `glIndexd` | `0x6F680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `glIndexdv` | `0x6F6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `glIndexf` | `0x6F6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `glIndexfv` | `0x6F6E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `glIndexi` | `0x6F700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `glIndexiv` | `0x6F720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `glIndexs` | `0x6F740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `glIndexsv` | `0x6F760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `glIndexub` | `0x6F780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `glIndexubv` | `0x6F7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `glLightModeliv` | `0x6F7C0` | 86 | UnwindData |  |
| 161 | `glLightiv` | `0x6F820` | 100 | UnwindData |  |
| 170 | `glMap1d` | `0x6F890` | 144 | UnwindData |  |
| 173 | `glMap2f` | `0x6F930` | 208 | UnwindData |  |
| 174 | `glMapGrid1d` | `0x6FA10` | 103 | UnwindData |  |
| 176 | `glMapGrid2d` | `0x6FA80` | 150 | UnwindData |  |
| 177 | `glMapGrid2f` | `0x6FB20` | 150 | UnwindData |  |
| 181 | `glMaterialiv` | `0x6FBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `glNormal3b` | `0x6FBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `glNormal3bv` | `0x6FC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `glNormal3i` | `0x6FC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `glNormal3iv` | `0x6FC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `glNormal3s` | `0x6FC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `glNormal3sv` | `0x6FC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `glPassThrough` | `0x6FCA0` | 80 | UnwindData |  |
| 199 | `glPixelMapfv` | `0x6FD00` | 100 | UnwindData |  |
| 200 | `glPixelMapuiv` | `0x6FD70` | 100 | UnwindData |  |
| 201 | `glPixelMapusv` | `0x6FDE0` | 100 | UnwindData |  |
| 202 | `glPixelStoref` | `0x6FE50` | 87 | UnwindData |  |
| 215 | `glPrioritizeTextures` | `0x6FEB0` | 102 | UnwindData |  |
| 220 | `glRasterPos2d` | `0x6FF20` | 96 | UnwindData |  |
| 221 | `glRasterPos2dv` | `0x6FF90` | 73 | UnwindData |  |
| 223 | `glRasterPos2fv` | `0x6FFE0` | 73 | UnwindData |  |
| 225 | `glRasterPos2iv` | `0x70030` | 73 | UnwindData |  |
| 226 | `glRasterPos2s` | `0x70080` | 88 | UnwindData |  |
| 227 | `glRasterPos2sv` | `0x700E0` | 73 | UnwindData |  |
| 231 | `glRasterPos3fv` | `0x70130` | 73 | UnwindData |  |
| 233 | `glRasterPos3iv` | `0x70180` | 73 | UnwindData |  |
| 234 | `glRasterPos3s` | `0x701D0` | 106 | UnwindData |  |
| 235 | `glRasterPos3sv` | `0x70240` | 73 | UnwindData |  |
| 236 | `glRasterPos4d` | `0x70290` | 137 | UnwindData |  |
| 237 | `glRasterPos4dv` | `0x70320` | 73 | UnwindData |  |
| 239 | `glRasterPos4fv` | `0x70370` | 73 | UnwindData |  |
| 241 | `glRasterPos4iv` | `0x703C0` | 73 | UnwindData |  |
| 242 | `glRasterPos4s` | `0x70410` | 126 | UnwindData |  |
| 243 | `glRasterPos4sv` | `0x704A0` | 73 | UnwindData |  |
| 246 | `glRectd` | `0x704F0` | 137 | UnwindData |  |
| 247 | `glRectdv` | `0x70580` | 88 | UnwindData |  |
| 249 | `glRectfv` | `0x705E0` | 88 | UnwindData |  |
| 250 | `glRecti` | `0x70640` | 118 | UnwindData |  |
| 251 | `glRectiv` | `0x706C0` | 88 | UnwindData |  |
| 252 | `glRects` | `0x70720` | 126 | UnwindData |  |
| 253 | `glRectsv` | `0x707B0` | 88 | UnwindData |  |
| 266 | `glTexCoord1dv` | `0x70810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `glTexCoord1fv` | `0x70830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `glTexCoord1i` | `0x70850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `glTexCoord1iv` | `0x70870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `glTexCoord1s` | `0x70890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `glTexCoord1sv` | `0x708B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `glTexCoord2iv` | `0x708D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `glTexCoord2s` | `0x708F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `glTexCoord2sv` | `0x70910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `glTexCoord3d` | `0x70930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `glTexCoord3dv` | `0x70950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `glTexCoord3fv` | `0x70970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `glTexCoord3i` | `0x70990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `glTexCoord3iv` | `0x709B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `glTexCoord3s` | `0x709D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `glTexCoord3sv` | `0x709F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `glTexCoord4dv` | `0x70A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `glTexCoord4fv` | `0x70A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `glTexCoord4i` | `0x70A50` | 31 | UnwindData |  |
| 294 | `glTexCoord4iv` | `0x70A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `glTexCoord4s` | `0x70AA0` | 31 | UnwindData |  |
| 296 | `glTexCoord4sv` | `0x70AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `glTexEnviv` | `0x70AF0` | 100 | UnwindData |  |
| 302 | `glTexGend` | `0x70B60` | 100 | UnwindData |  |
| 304 | `glTexGenf` | `0x70BD0` | 100 | UnwindData |  |
| 307 | `glTexGeniv` | `0x70C40` | 100 | UnwindData |  |
| 323 | `glVertex2iv` | `0x70CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `glVertex2sv` | `0x70CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `glVertex3i` | `0x70CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `glVertex3iv` | `0x70D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `glVertex3s` | `0x70D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `glVertex3sv` | `0x70D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `glVertex4d` | `0x70D70` | 31 | UnwindData |  |
| 335 | `glVertex4dv` | `0x70DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `glVertex4fv` | `0x70DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `glVertex4i` | `0x70DE0` | 31 | UnwindData |  |
| 339 | `glVertex4iv` | `0x70E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `glVertex4s` | `0x70E30` | 31 | UnwindData |  |
| 341 | `glVertex4sv` | `0x70E60` | 377,004 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
