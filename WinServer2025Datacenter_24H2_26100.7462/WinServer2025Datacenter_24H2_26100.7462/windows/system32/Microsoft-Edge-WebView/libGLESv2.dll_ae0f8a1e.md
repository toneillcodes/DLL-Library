# Binary Specification: libGLESv2.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Microsoft-Edge-WebView\libGLESv2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ae0f8a1ed8fb102c2fffe505b55e449dc44978a1239fab3b7505739ef3ef16b0`
* **Total Exported Functions:** 1807

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `EGL_ChooseConfig` | `0x7620` | 596 | UnwindData |  |
| 7 | `EGL_CopyBuffers` | `0x7880` | 435 | UnwindData |  |
| 9 | `EGL_CreateContext` | `0x7A40` | 574 | UnwindData |  |
| 15 | `EGL_CreatePbufferSurface` | `0x7C80` | 559 | UnwindData |  |
| 16 | `EGL_CreatePixmapSurface` | `0x7EB0` | 574 | UnwindData |  |
| 25 | `EGL_CreateWindowSurface` | `0x80F0` | 638 | UnwindData |  |
| 27 | `EGL_DestroyContext` | `0x8370` | 429 | UnwindData |  |
| 31 | `EGL_DestroySurface` | `0x8520` | 486 | UnwindData |  |
| 39 | `EGL_GetConfigAttrib` | `0x8710` | 488 | UnwindData |  |
| 40 | `EGL_GetConfigs` | `0x8900` | 433 | UnwindData |  |
| 42 | `EGL_GetCurrentDisplay` | `0x8AC0` | 195 | UnwindData |  |
| 43 | `EGL_GetCurrentSurface` | `0x8B90` | 340 | UnwindData |  |
| 44 | `EGL_GetDisplay` | `0x8CF0` | 371 | UnwindData |  |
| 45 | `EGL_GetError` | `0x8E70` | 180 | UnwindData |  |
| 53 | `EGL_GetProcAddress` | `0x8F30` | 390 | UnwindData |  |
| 58 | `EGL_Initialize` | `0x90C0` | 564 | UnwindData |  |
| 62 | `EGL_MakeCurrent` | `0x9300` | 466 | UnwindData |  |
| 71 | `EGL_QueryContext` | `0x94E0` | 429 | UnwindData |  |
| 81 | `EGL_QueryString` | `0x9690` | 500 | UnwindData |  |
| 84 | `EGL_QuerySurface` | `0x9890` | 456 | UnwindData |  |
| 104 | `EGL_SwapBuffers` | `0x9A60` | 463 | UnwindData |  |
| 107 | `EGL_Terminate` | `0x9C30` | 544 | UnwindData |  |
| 111 | `EGL_WaitGL` | `0x9E50` | 340 | UnwindData |  |
| 112 | `EGL_WaitNative` | `0x9FB0` | 385 | UnwindData |  |
| 3 | `EGL_BindTexImage` | `0xA140` | 397 | UnwindData |  |
| 91 | `EGL_ReleaseTexImage` | `0xA2D0` | 397 | UnwindData |  |
| 103 | `EGL_SurfaceAttrib` | `0xA460` | 415 | UnwindData |  |
| 106 | `EGL_SwapInterval` | `0xA600` | 515 | UnwindData |  |
| 2 | `EGL_BindAPI` | `0xA810` | 333 | UnwindData |  |
| 14 | `EGL_CreatePbufferFromClientBuffer` | `0xA960` | 602 | UnwindData |  |
| 70 | `EGL_QueryAPI` | `0xABC0` | 261 | UnwindData |  |
| 92 | `EGL_ReleaseThread` | `0xACD0` | 411 | UnwindData |  |
| 110 | `EGL_WaitClient` | `0xAE70` | 340 | UnwindData |  |
| 41 | `EGL_GetCurrentContext` | `0xAFD0` | 191 | UnwindData |  |
| 5 | `EGL_ClientWaitSync` | `0xB090` | 512 | UnwindData |  |
| 11 | `EGL_CreateImage` | `0xB290` | 708 | UnwindData |  |
| 17 | `EGL_CreatePlatformPixmapSurface` | `0xB560` | 583 | UnwindData |  |
| 19 | `EGL_CreatePlatformWindowSurface` | `0xB7B0` | 651 | UnwindData |  |
| 23 | `EGL_CreateSync` | `0xBA40` | 676 | UnwindData |  |
| 28 | `EGL_DestroyImage` | `0xBCF0` | 445 | UnwindData |  |
| 32 | `EGL_DestroySync` | `0xBEB0` | 515 | UnwindData |  |
| 51 | `EGL_GetPlatformDisplay` | `0xC0C0` | 573 | UnwindData |  |
| 54 | `EGL_GetSyncAttrib` | `0xC300` | 447 | UnwindData |  |
| 113 | `EGL_WaitSync` | `0xC4C0` | 460 | UnwindData |  |
| 93 | `EGL_SetBlobCacheFuncsANDROID` | `0xC690` | 420 | UnwindData |  |
| 13 | `EGL_CreateNativeClientBufferANDROID` | `0xC840` | 478 | UnwindData |  |
| 38 | `EGL_GetCompositorTimingSupportedANDROID` | `0xCA20` | 426 | UnwindData |  |
| 37 | `EGL_GetCompositorTimingANDROID` | `0xCBD0` | 498 | UnwindData |  |
| 50 | `EGL_GetNextFrameIdANDROID` | `0xCDD0` | 397 | UnwindData |  |
| 46 | `EGL_GetFrameTimestampSupportedANDROID` | `0xCF60` | 426 | UnwindData |  |
| 47 | `EGL_GetFrameTimestampsANDROID` | `0xD110` | 523 | UnwindData |  |
| 49 | `EGL_GetNativeClientBufferANDROID` | `0xD320` | 344 | UnwindData |  |
| 34 | `EGL_DupNativeFenceFDANDROID` | `0xD480` | 387 | UnwindData |  |
| 65 | `EGL_PresentationTimeANDROID` | `0xD610` | 397 | UnwindData |  |
| 10 | `EGL_CreateDeviceANGLE` | `0xD7A0` | 356 | UnwindData |  |
| 88 | `EGL_ReleaseDeviceANGLE` | `0xD910` | 351 | UnwindData |  |
| 61 | `EGL_LockVulkanQueueANGLE` | `0xDA70` | 368 | UnwindData |  |
| 109 | `EGL_UnlockVulkanQueueANGLE` | `0xDBE0` | 368 | UnwindData |  |
| 1 | `EGL_AcquireExternalContextANGLE` | `0xDD50` | 377 | UnwindData |  |
| 89 | `EGL_ReleaseExternalContextANGLE` | `0xDED0` | 430 | UnwindData |  |
| 82 | `EGL_QueryStringiANGLE` | `0xE080` | 402 | UnwindData |  |
| 75 | `EGL_QueryDisplayAttribANGLE` | `0xE220` | 435 | UnwindData |  |
| 8 | `EGL_CopyMetalSharedEventANGLE` | `0xE3E0` | 386 | UnwindData |  |
| 95 | `EGL_SetValidationEnabledANGLE` | `0xE570` | 349 | UnwindData |  |
| 90 | `EGL_ReleaseHighPowerGPUANGLE` | `0xE6D0` | 424 | UnwindData |  |
| 87 | `EGL_ReacquireHighPowerGPUANGLE` | `0xE880` | 424 | UnwindData |  |
| 57 | `EGL_HandleGPUSwitchANGLE` | `0xEA30` | 360 | UnwindData |  |
| 36 | `EGL_ForceGPUSwitchANGLE` | `0xEBA0` | 383 | UnwindData |  |
| 64 | `EGL_PrepareSwapBuffersANGLE` | `0xED20` | 435 | UnwindData |  |
| 66 | `EGL_ProgramCacheGetAttribANGLE` | `0xEEE0` | 469 | UnwindData |  |
| 68 | `EGL_ProgramCacheQueryANGLE` | `0xF0C0` | 447 | UnwindData |  |
| 67 | `EGL_ProgramCachePopulateANGLE` | `0xF280` | 427 | UnwindData |  |
| 69 | `EGL_ProgramCacheResizeANGLE` | `0xF430` | 537 | UnwindData |  |
| 86 | `EGL_QuerySurfacePointerANGLE` | `0xF650` | 417 | UnwindData |  |
| 22 | `EGL_CreateStreamProducerD3DTextureANGLE` | `0xF800` | 561 | UnwindData |  |
| 102 | `EGL_StreamPostD3DTextureANGLE` | `0xFA40` | 670 | UnwindData |  |
| 48 | `EGL_GetMscRateANGLE` | `0xFCE0` | 450 | UnwindData |  |
| 35 | `EGL_ExportVkImageANGLE` | `0xFEB0` | 417 | UnwindData |  |
| 115 | `EGL_WaitUntilWorkScheduledANGLE` | `0x10060` | 360 | UnwindData |  |
| 56 | `EGL_GetSyncValuesCHROMIUM` | `0x101D0` | 477 | UnwindData |  |
| 73 | `EGL_QueryDeviceAttribEXT` | `0x103B0` | 356 | UnwindData |  |
| 74 | `EGL_QueryDeviceStringEXT` | `0x10520` | 381 | UnwindData |  |
| 76 | `EGL_QueryDisplayAttribEXT` | `0x106A0` | 435 | UnwindData |  |
| 77 | `EGL_QueryDmaBufFormatsEXT` | `0x10860` | 492 | UnwindData |  |
| 78 | `EGL_QueryDmaBufModifiersEXT` | `0x10A50` | 457 | UnwindData |  |
| 18 | `EGL_CreatePlatformPixmapSurfaceEXT` | `0x10C20` | 613 | UnwindData |  |
| 20 | `EGL_CreatePlatformWindowSurfaceEXT` | `0x10E90` | 684 | UnwindData |  |
| 52 | `EGL_GetPlatformDisplayEXT` | `0x11140` | 571 | UnwindData |  |
| 83 | `EGL_QuerySupportedCompressionRatesEXT` | `0x11380` | 458 | UnwindData |  |
| 26 | `EGL_DebugMessageControlKHR` | `0x11550` | 553 | UnwindData |  |
| 59 | `EGL_LabelObjectKHR` | `0x11780` | 669 | UnwindData |  |
| 72 | `EGL_QueryDebugKHR` | `0x11A20` | 513 | UnwindData |  |
| 6 | `EGL_ClientWaitSyncKHR` | `0x11C30` | 512 | UnwindData |  |
| 24 | `EGL_CreateSyncKHR` | `0x11E30` | 674 | UnwindData |  |
| 33 | `EGL_DestroySyncKHR` | `0x120E0` | 515 | UnwindData |  |
| 55 | `EGL_GetSyncAttribKHR` | `0x122F0` | 447 | UnwindData |  |
| 12 | `EGL_CreateImageKHR` | `0x124B0` | 773 | UnwindData |  |
| 29 | `EGL_DestroyImageKHR` | `0x127C0` | 408 | UnwindData |  |
| 60 | `EGL_LockSurfaceKHR` | `0x12960` | 559 | UnwindData |  |
| 85 | `EGL_QuerySurface64KHR` | `0x12B90` | 456 | UnwindData |  |
| 108 | `EGL_UnlockSurfaceKHR` | `0x12D60` | 384 | UnwindData |  |
| 94 | `EGL_SetDamageRegionKHR` | `0x12EE0` | 414 | UnwindData |  |
| 96 | `EGL_SignalSyncKHR` | `0x13080` | 397 | UnwindData |  |
| 21 | `EGL_CreateStreamKHR` | `0x13210` | 535 | UnwindData |  |
| 30 | `EGL_DestroyStreamKHR` | `0x13430` | 472 | UnwindData |  |
| 79 | `EGL_QueryStreamKHR` | `0x13610` | 451 | UnwindData |  |
| 80 | `EGL_QueryStreamu64KHR` | `0x137E0` | 438 | UnwindData |  |
| 97 | `EGL_StreamAttribKHR` | `0x139A0` | 429 | UnwindData |  |
| 98 | `EGL_StreamConsumerAcquireKHR` | `0x13B50` | 384 | UnwindData |  |
| 100 | `EGL_StreamConsumerGLTextureExternalKHR` | `0x13CD0` | 384 | UnwindData |  |
| 101 | `EGL_StreamConsumerReleaseKHR` | `0x13E50` | 384 | UnwindData |  |
| 105 | `EGL_SwapBuffersWithDamageKHR` | `0x13FD0` | 496 | UnwindData |  |
| 114 | `EGL_WaitSyncKHR` | `0x141C0` | 460 | UnwindData |  |
| 63 | `EGL_PostSubBufferNV` | `0x14390` | 453 | UnwindData |  |
| 99 | `EGL_StreamConsumerGLTextureExternalAttribsNV` | `0x14560` | 561 | UnwindData |  |
| 120 | `GL_AlphaFunc` | `0x147A0` | 271 | UnwindData |  |
| 121 | `GL_AlphaFuncx` | `0x148B0` | 266 | UnwindData |  |
| 185 | `GL_ClearColorx` | `0x149C0` | 247 | UnwindData |  |
| 187 | `GL_ClearDepthx` | `0x14AC0` | 198 | UnwindData |  |
| 191 | `GL_ClientActiveTexture` | `0x14B90` | 221 | UnwindData |  |
| 194 | `GL_ClipPlanef` | `0x14C70` | 226 | UnwindData |  |
| 195 | `GL_ClipPlanex` | `0x14D60` | 432 | UnwindData |  |
| 196 | `GL_Color4f` | `0x14F10` | 370 | UnwindData |  |
| 197 | `GL_Color4ub` | `0x15090` | 343 | UnwindData |  |
| 198 | `GL_Color4x` | `0x151F0` | 328 | UnwindData |  |
| 203 | `GL_ColorPointer` | `0x15340` | 526 | UnwindData |  |
| 266 | `GL_DepthRangex` | `0x15550` | 282 | UnwindData |  |
| 269 | `GL_DisableClientState` | `0x15670` | 271 | UnwindData |  |
| 317 | `GL_EnableClientState` | `0x15780` | 271 | UnwindData |  |
| 334 | `GL_Fogf` | `0x15890` | 329 | UnwindData |  |
| 335 | `GL_Fogfv` | `0x159E0` | 212 | UnwindData |  |
| 336 | `GL_Fogx` | `0x15AC0` | 467 | UnwindData |  |
| 337 | `GL_Fogxv` | `0x15CA0` | 425 | UnwindData |  |
| 363 | `GL_Frustumf` | `0x15E50` | 657 | UnwindData |  |
| 364 | `GL_Frustumx` | `0x160F0` | 537 | UnwindData |  |
| 403 | `GL_GetClipPlanef` | `0x16310` | 226 | UnwindData |  |
| 404 | `GL_GetClipPlanex` | `0x16400` | 608 | UnwindData |  |
| 410 | `GL_GetFixedv` | `0x16660` | 342 | UnwindData |  |
| 440 | `GL_GetLightfv` | `0x167C0` | 366 | UnwindData |  |
| 441 | `GL_GetLightxv` | `0x16930` | 468 | UnwindData |  |
| 442 | `GL_GetMaterialfv` | `0x16B10` | 238 | UnwindData |  |
| 443 | `GL_GetMaterialxv` | `0x16C00` | 491 | UnwindData |  |
| 516 | `GL_GetTexEnvfv` | `0x16DF0` | 271 | UnwindData |  |
| 517 | `GL_GetTexEnviv` | `0x16F00` | 397 | UnwindData |  |
| 518 | `GL_GetTexEnvxv` | `0x17090` | 397 | UnwindData |  |
| 541 | `GL_GetTexParameterxv` | `0x17220` | 244 | UnwindData |  |
| 610 | `GL_LightModelf` | `0x17320` | 271 | UnwindData |  |
| 611 | `GL_LightModelfv` | `0x17430` | 258 | UnwindData |  |
| 612 | `GL_LightModelx` | `0x17540` | 278 | UnwindData |  |
| 613 | `GL_LightModelxv` | `0x17660` | 457 | UnwindData |  |
| 614 | `GL_Lightf` | `0x17830` | 434 | UnwindData |  |
| 615 | `GL_Lightfv` | `0x179F0` | 243 | UnwindData |  |
| 616 | `GL_Lightx` | `0x17AF0` | 468 | UnwindData |  |
| 617 | `GL_Lightxv` | `0x17CD0` | 481 | UnwindData |  |
| 619 | `GL_LineWidthx` | `0x17EC0` | 206 | UnwindData |  |
| 621 | `GL_LoadIdentity` | `0x17F90` | 278 | UnwindData |  |
| 622 | `GL_LoadMatrixf` | `0x180B0` | 284 | UnwindData |  |
| 623 | `GL_LoadMatrixx` | `0x181D0` | 537 | UnwindData |  |
| 625 | `GL_LogicOp` | `0x183F0` | 209 | UnwindData |  |
| 631 | `GL_Materialf` | `0x184D0` | 347 | UnwindData |  |
| 632 | `GL_Materialfv` | `0x18630` | 295 | UnwindData |  |
| 633 | `GL_Materialx` | `0x18760` | 380 | UnwindData |  |
| 634 | `GL_Materialxv` | `0x188E0` | 399 | UnwindData |  |
| 636 | `GL_MatrixMode` | `0x18A70` | 212 | UnwindData |  |
| 643 | `GL_MultMatrixf` | `0x18B50` | 284 | UnwindData |  |
| 644 | `GL_MultMatrixx` | `0x18C70` | 537 | UnwindData |  |
| 656 | `GL_MultiTexCoord4f` | `0x18E90` | 381 | UnwindData |  |
| 657 | `GL_MultiTexCoord4x` | `0x19010` | 345 | UnwindData |  |
| 658 | `GL_Normal3f` | `0x19170` | 248 | UnwindData |  |
| 659 | `GL_Normal3x` | `0x19270` | 224 | UnwindData |  |
| 660 | `GL_NormalPointer` | `0x19350` | 631 | UnwindData |  |
| 665 | `GL_Orthof` | `0x195D0` | 659 | UnwindData |  |
| 666 | `GL_Orthox` | `0x19870` | 543 | UnwindData |  |
| 673 | `GL_PointParameterf` | `0x19A90` | 334 | UnwindData |  |
| 674 | `GL_PointParameterfv` | `0x19BE0` | 422 | UnwindData |  |
| 675 | `GL_PointParameterx` | `0x19D90` | 339 | UnwindData |  |
| 676 | `GL_PointParameterxv` | `0x19EF0` | 508 | UnwindData |  |
| 677 | `GL_PointSize` | `0x1A0F0` | 215 | UnwindData |  |
| 679 | `GL_PointSizex` | `0x1A1D0` | 222 | UnwindData |  |
| 684 | `GL_PolygonOffsetx` | `0x1A2B0` | 211 | UnwindData |  |
| 688 | `GL_PopMatrix` | `0x1A390` | 215 | UnwindData |  |
| 766 | `GL_PushMatrix` | `0x1A470` | 215 | UnwindData |  |
| 785 | `GL_Rotatef` | `0x1A550` | 467 | UnwindData |  |
| 786 | `GL_Rotatex` | `0x1A730` | 381 | UnwindData |  |
| 788 | `GL_SampleCoveragex` | `0x1A8B0` | 213 | UnwindData |  |
| 805 | `GL_Scalef` | `0x1A990` | 402 | UnwindData |  |
| 806 | `GL_Scalex` | `0x1AB30` | 342 | UnwindData |  |
| 811 | `GL_ShadeModel` | `0x1AC90` | 228 | UnwindData |  |
| 832 | `GL_TexCoordPointer` | `0x1AD80` | 528 | UnwindData |  |
| 833 | `GL_TexEnvf` | `0x1AF90` | 400 | UnwindData |  |
| 834 | `GL_TexEnvfv` | `0x1B120` | 276 | UnwindData |  |
| 835 | `GL_TexEnvi` | `0x1B240` | 408 | UnwindData |  |
| 836 | `GL_TexEnviv` | `0x1B3E0` | 468 | UnwindData |  |
| 837 | `GL_TexEnvx` | `0x1B5C0` | 455 | UnwindData |  |
| 838 | `GL_TexEnvxv` | `0x1B790` | 448 | UnwindData |  |
| 865 | `GL_TexParameterx` | `0x1B950` | 375 | UnwindData |  |
| 866 | `GL_TexParameterxv` | `0x1BAD0` | 394 | UnwindData |  |
| 892 | `GL_Translatef` | `0x1BC60` | 413 | UnwindData |  |
| 893 | `GL_Translatex` | `0x1BE00` | 353 | UnwindData |  |
| 957 | `GL_VertexPointer` | `0x1BF70` | 520 | UnwindData |  |
| 119 | `GL_ActiveTexture` | `0x1C180` | 219 | UnwindData |  |
| 122 | `GL_AttachShader` | `0x1C260` | 204 | UnwindData |  |
| 128 | `GL_BindAttribLocation` | `0x1C330` | 227 | UnwindData |  |
| 129 | `GL_BindBuffer` | `0x1C420` | 991 | UnwindData |  |
| 134 | `GL_BindFramebuffer` | `0x1C800` | 454 | UnwindData |  |
| 139 | `GL_BindRenderbuffer` | `0x1C9D0` | 256 | UnwindData |  |
| 142 | `GL_BindTexture` | `0x1CAD0` | 720 | UnwindData |  |
| 150 | `GL_BlendColor` | `0x1CDA0` | 273 | UnwindData |  |
| 151 | `GL_BlendEquation` | `0x1CEC0` | 283 | UnwindData |  |
| 153 | `GL_BlendEquationSeparate` | `0x1CFE0` | 407 | UnwindData |  |
| 160 | `GL_BlendFunc` | `0x1D180` | 194 | UnwindData |  |
| 161 | `GL_BlendFuncSeparate` | `0x1D250` | 260 | UnwindData |  |
| 172 | `GL_BufferData` | `0x1D360` | 319 | UnwindData |  |
| 176 | `GL_BufferSubData` | `0x1D4A0` | 312 | UnwindData |  |
| 177 | `GL_CheckFramebufferStatus` | `0x1D5E0` | 341 | UnwindData |  |
| 179 | `GL_Clear` | `0x1D740` | 141 | UnwindData |  |
| 1025 | `glClear` | `0x1D740` | 141 | UnwindData |  |
| 184 | `GL_ClearColor` | `0x1D7D0` | 214 | UnwindData |  |
| 1030 | `glClearColor` | `0x1D7D0` | 214 | UnwindData |  |
| 186 | `GL_ClearDepthf` | `0x1D8B0` | 149 | UnwindData |  |
| 1032 | `glClearDepthf` | `0x1D8B0` | 149 | UnwindData |  |
| 188 | `GL_ClearStencil` | `0x1D950` | 111 | UnwindData |  |
| 1034 | `glClearStencil` | `0x1D950` | 111 | UnwindData |  |
| 199 | `GL_ColorMask` | `0x1D9C0` | 169 | UnwindData |  |
| 1045 | `glColorMask` | `0x1D9C0` | 169 | UnwindData |  |
| 204 | `GL_CompileShader` | `0x1DA70` | 196 | UnwindData |  |
| 206 | `GL_CompressedTexImage2D` | `0x1DB40` | 332 | UnwindData |  |
| 211 | `GL_CompressedTexSubImage2D` | `0x1DC90` | 353 | UnwindData |  |
| 222 | `GL_CopyTexImage2D` | `0x1DE00` | 533 | UnwindData |  |
| 223 | `GL_CopyTexSubImage2D` | `0x1E020` | 533 | UnwindData |  |
| 230 | `GL_CreateProgram` | `0x1E240` | 255 | UnwindData |  |
| 231 | `GL_CreateShader` | `0x1E340` | 307 | UnwindData |  |
| 234 | `GL_CullFace` | `0x1E480` | 202 | UnwindData |  |
| 242 | `GL_DeleteBuffers` | `0x1E550` | 286 | UnwindData |  |
| 244 | `GL_DeleteFramebuffers` | `0x1E670` | 254 | UnwindData |  |
| 248 | `GL_DeleteProgram` | `0x1E770` | 206 | UnwindData |  |
| 253 | `GL_DeleteRenderbuffers` | `0x1E840` | 318 | UnwindData |  |
| 257 | `GL_DeleteShader` | `0x1E980` | 203 | UnwindData |  |
| 259 | `GL_DeleteTextures` | `0x1EA50` | 222 | UnwindData |  |
| 263 | `GL_DepthFunc` | `0x1EB30` | 173 | UnwindData |  |
| 264 | `GL_DepthMask` | `0x1EBE0` | 124 | UnwindData |  |
| 1110 | `glDepthMask` | `0x1EBE0` | 124 | UnwindData |  |
| 265 | `GL_DepthRangef` | `0x1EC60` | 291 | UnwindData |  |
| 267 | `GL_DetachShader` | `0x1ED90` | 204 | UnwindData |  |
| 268 | `GL_Disable` | `0x1EE60` | 161 | UnwindData |  |
| 271 | `GL_DisableVertexAttribArray` | `0x1EF10` | 258 | UnwindData |  |
| 278 | `GL_DrawArrays` | `0x1F020` | 1,660 | UnwindData |  |
| 287 | `GL_DrawElements` | `0x1F6A0` | 2,249 | UnwindData |  |
| 316 | `GL_Enable` | `0x1FF70` | 161 | UnwindData |  |
| 318 | `GL_EnableVertexAttribArray` | `0x20020` | 258 | UnwindData |  |
| 329 | `GL_Finish` | `0x20130` | 160 | UnwindData |  |
| 1175 | `glFinish` | `0x20130` | 160 | UnwindData |  |
| 331 | `GL_Flush` | `0x201D0` | 160 | UnwindData |  |
| 1177 | `glFlush` | `0x201D0` | 160 | UnwindData |  |
| 349 | `GL_FramebufferRenderbuffer` | `0x20270` | 462 | UnwindData |  |
| 353 | `GL_FramebufferTexture2D` | `0x20440` | 498 | UnwindData |  |
| 362 | `GL_FrontFace` | `0x20640` | 173 | UnwindData |  |
| 365 | `GL_GenBuffers` | `0x206F0` | 284 | UnwindData |  |
| 367 | `GL_GenFramebuffers` | `0x20810` | 314 | UnwindData |  |
| 374 | `GL_GenRenderbuffers` | `0x20950` | 314 | UnwindData |  |
| 378 | `GL_GenTextures` | `0x20A90` | 284 | UnwindData |  |
| 382 | `GL_GenerateMipmap` | `0x20BB0` | 264 | UnwindData |  |
| 384 | `GL_GetActiveAttrib` | `0x20CC0` | 367 | UnwindData |  |
| 385 | `GL_GetActiveUniform` | `0x20E30` | 412 | UnwindData |  |
| 390 | `GL_GetAttachedShaders` | `0x20FD0` | 283 | UnwindData |  |
| 391 | `GL_GetAttribLocation` | `0x210F0` | 198 | UnwindData |  |
| 394 | `GL_GetBooleanv` | `0x211C0` | 311 | UnwindData |  |
| 398 | `GL_GetBufferParameteriv` | `0x21300` | 275 | UnwindData |  |
| 408 | `GL_GetError` | `0x21420` | 111 | UnwindData |  |
| 1254 | `glGetError` | `0x21420` | 111 | UnwindData |  |
| 411 | `GL_GetFloatv` | `0x21490` | 369 | UnwindData |  |
| 416 | `GL_GetFramebufferAttachmentParameteriv` | `0x21610` | 290 | UnwindData |  |
| 436 | `GL_GetIntegerv` | `0x21740` | 363 | UnwindData |  |
| 465 | `GL_GetProgramInfoLog` | `0x218B0` | 262 | UnwindData |  |
| 477 | `GL_GetProgramiv` | `0x219C0` | 216 | UnwindData |  |
| 492 | `GL_GetRenderbufferParameteriv` | `0x21AA0` | 236 | UnwindData |  |
| 508 | `GL_GetShaderInfoLog` | `0x21B90` | 251 | UnwindData |  |
| 509 | `GL_GetShaderPrecisionFormat` | `0x21C90` | 296 | UnwindData |  |
| 510 | `GL_GetShaderSource` | `0x21DC0` | 254 | UnwindData |  |
| 511 | `GL_GetShaderiv` | `0x21EC0` | 280 | UnwindData |  |
| 513 | `GL_GetString` | `0x21FE0` | 208 | UnwindData |  |
| 537 | `GL_GetTexParameterfv` | `0x220B0` | 242 | UnwindData |  |
| 539 | `GL_GetTexParameteriv` | `0x221B0` | 242 | UnwindData |  |
| 546 | `GL_GetUniformLocation` | `0x222B0` | 198 | UnwindData |  |
| 547 | `GL_GetUniformfv` | `0x22380` | 222 | UnwindData |  |
| 549 | `GL_GetUniformiv` | `0x22460` | 222 | UnwindData |  |
| 559 | `GL_GetVertexAttribPointerv` | `0x22540` | 294 | UnwindData |  |
| 561 | `GL_GetVertexAttribfv` | `0x22670` | 236 | UnwindData |  |
| 563 | `GL_GetVertexAttribiv` | `0x22760` | 236 | UnwindData |  |
| 576 | `GL_Hint` | `0x22850` | 393 | UnwindData |  |
| 585 | `GL_IsBuffer` | `0x229E0` | 123 | UnwindData |  |
| 1431 | `glIsBuffer` | `0x229E0` | 123 | UnwindData |  |
| 586 | `GL_IsEnabled` | `0x22A60` | 153 | UnwindData |  |
| 591 | `GL_IsFramebuffer` | `0x22B00` | 170 | UnwindData |  |
| 594 | `GL_IsProgram` | `0x22BB0` | 154 | UnwindData |  |
| 599 | `GL_IsRenderbuffer` | `0x22C50` | 170 | UnwindData |  |
| 603 | `GL_IsShader` | `0x22D00` | 170 | UnwindData |  |
| 605 | `GL_IsTexture` | `0x22DB0` | 107 | UnwindData |  |
| 1451 | `glIsTexture` | `0x22DB0` | 107 | UnwindData |  |
| 618 | `GL_LineWidth` | `0x22E20` | 177 | UnwindData |  |
| 1464 | `glLineWidth` | `0x22E20` | 177 | UnwindData |  |
| 620 | `GL_LinkProgram` | `0x22EE0` | 256 | UnwindData |  |
| 672 | `GL_PixelStorei` | `0x22FE0` | 436 | UnwindData |  |
| 682 | `GL_PolygonOffset` | `0x231A0` | 184 | UnwindData |  |
| 1528 | `glPolygonOffset` | `0x231A0` | 184 | UnwindData |  |
| 770 | `GL_ReadPixels` | `0x23260` | 520 | UnwindData |  |
| 776 | `GL_ReleaseShaderCompiler` | `0x23470` | 223 | UnwindData |  |
| 778 | `GL_RenderbufferStorage` | `0x23550` | 296 | UnwindData |  |
| 787 | `GL_SampleCoverage` | `0x23680` | 163 | UnwindData |  |
| 1633 | `glSampleCoverage` | `0x23680` | 163 | UnwindData |  |
| 807 | `GL_Scissor` | `0x23730` | 226 | UnwindData |  |
| 812 | `GL_ShaderBinary` | `0x23820` | 320 | UnwindData |  |
| 813 | `GL_ShaderSource` | `0x23960` | 251 | UnwindData |  |
| 819 | `GL_StencilFunc` | `0x23A60` | 293 | UnwindData |  |
| 820 | `GL_StencilFuncSeparate` | `0x23B90` | 402 | UnwindData |  |
| 821 | `GL_StencilMask` | `0x23D30` | 147 | UnwindData |  |
| 1667 | `glStencilMask` | `0x23D30` | 147 | UnwindData |  |
| 822 | `GL_StencilMaskSeparate` | `0x23DD0` | 299 | UnwindData |  |
| 823 | `GL_StencilOp` | `0x23F00` | 276 | UnwindData |  |
| 824 | `GL_StencilOpSeparate` | `0x24020` | 438 | UnwindData |  |
| 845 | `GL_TexImage2D` | `0x241E0` | 353 | UnwindData |  |
| 859 | `GL_TexParameterf` | `0x24350` | 338 | UnwindData |  |
| 860 | `GL_TexParameterfv` | `0x244B0` | 251 | UnwindData |  |
| 862 | `GL_TexParameteri` | `0x245B0` | 335 | UnwindData |  |
| 863 | `GL_TexParameteriv` | `0x24700` | 251 | UnwindData |  |
| 885 | `GL_TexSubImage2D` | `0x24800` | 353 | UnwindData |  |
| 894 | `GL_Uniform1f` | `0x24970` | 394 | UnwindData |  |
| 895 | `GL_Uniform1fv` | `0x24B00` | 335 | UnwindData |  |
| 896 | `GL_Uniform1i` | `0x24C50` | 388 | UnwindData |  |
| 897 | `GL_Uniform1iv` | `0x24DE0` | 292 | UnwindData |  |
| 900 | `GL_Uniform2f` | `0x24F10` | 423 | UnwindData |  |
| 901 | `GL_Uniform2fv` | `0x250C0` | 335 | UnwindData |  |
| 902 | `GL_Uniform2i` | `0x25210` | 386 | UnwindData |  |
| 903 | `GL_Uniform2iv` | `0x253A0` | 335 | UnwindData |  |
| 906 | `GL_Uniform3f` | `0x254F0` | 458 | UnwindData |  |
| 907 | `GL_Uniform3fv` | `0x256C0` | 335 | UnwindData |  |
| 908 | `GL_Uniform3i` | `0x25810` | 403 | UnwindData |  |
| 909 | `GL_Uniform3iv` | `0x259B0` | 335 | UnwindData |  |
| 912 | `GL_Uniform4f` | `0x25B00` | 527 | UnwindData |  |
| 913 | `GL_Uniform4fv` | `0x25D10` | 335 | UnwindData |  |
| 914 | `GL_Uniform4i` | `0x25E60` | 424 | UnwindData |  |
| 915 | `GL_Uniform4iv` | `0x26010` | 335 | UnwindData |  |
| 919 | `GL_UniformMatrix2fv` | `0x26160` | 304 | UnwindData |  |
| 922 | `GL_UniformMatrix3fv` | `0x26290` | 304 | UnwindData |  |
| 925 | `GL_UniformMatrix4fv` | `0x263C0` | 304 | UnwindData |  |
| 930 | `GL_UseProgram` | `0x264F0` | 191 | UnwindData |  |
| 933 | `GL_ValidateProgram` | `0x265B0` | 192 | UnwindData |  |
| 936 | `GL_VertexAttrib1f` | `0x26670` | 379 | UnwindData |  |
| 937 | `GL_VertexAttrib1fv` | `0x267F0` | 397 | UnwindData |  |
| 938 | `GL_VertexAttrib2f` | `0x26980` | 406 | UnwindData |  |
| 939 | `GL_VertexAttrib2fv` | `0x26B20` | 409 | UnwindData |  |
| 940 | `GL_VertexAttrib3f` | `0x26CC0` | 438 | UnwindData |  |
| 941 | `GL_VertexAttrib3fv` | `0x26E80` | 414 | UnwindData |  |
| 942 | `GL_VertexAttrib4f` | `0x27020` | 482 | UnwindData |  |
| 943 | `GL_VertexAttrib4fv` | `0x27210` | 227 | UnwindData |  |
| 955 | `GL_VertexAttribPointer` | `0x27300` | 1,127 | UnwindData |  |
| 958 | `GL_Viewport` | `0x27770` | 188 | UnwindData |  |
| 125 | `GL_BeginQuery` | `0x281F0` | 281 | UnwindData |  |
| 127 | `GL_BeginTransformFeedback` | `0x28310` | 446 | UnwindData |  |
| 130 | `GL_BindBufferBase` | `0x284D0` | 281 | UnwindData |  |
| 131 | `GL_BindBufferRange` | `0x285F0` | 363 | UnwindData |  |
| 141 | `GL_BindSampler` | `0x28760` | 249 | UnwindData |  |
| 143 | `GL_BindTransformFeedback` | `0x28860` | 294 | UnwindData |  |
| 145 | `GL_BindVertexArray` | `0x28990` | 253 | UnwindData |  |
| 168 | `GL_BlitFramebuffer` | `0x28A90` | 693 | UnwindData |  |
| 180 | `GL_ClearBufferfi` | `0x28D50` | 326 | UnwindData |  |
| 181 | `GL_ClearBufferfv` | `0x28EA0` | 227 | UnwindData |  |
| 182 | `GL_ClearBufferiv` | `0x28F90` | 227 | UnwindData |  |
| 183 | `GL_ClearBufferuiv` | `0x29080` | 227 | UnwindData |  |
| 192 | `GL_ClientWaitSync` | `0x29170` | 429 | UnwindData |  |
| 208 | `GL_CompressedTexImage3D` | `0x29320` | 404 | UnwindData |  |
| 213 | `GL_CompressedTexSubImage3D` | `0x294C0` | 477 | UnwindData |  |
| 216 | `GL_CopyBufferSubData` | `0x296A0` | 377 | UnwindData |  |
| 224 | `GL_CopyTexSubImage3D` | `0x29820` | 808 | UnwindData |  |
| 251 | `GL_DeleteQueries` | `0x29B50` | 215 | UnwindData |  |
| 255 | `GL_DeleteSamplers` | `0x29C30` | 209 | UnwindData |  |
| 258 | `GL_DeleteSync` | `0x29D10` | 228 | UnwindData |  |
| 260 | `GL_DeleteTransformFeedbacks` | `0x29E00` | 313 | UnwindData |  |
| 261 | `GL_DeleteVertexArrays` | `0x29F40` | 215 | UnwindData |  |
| 280 | `GL_DrawArraysInstanced` | `0x2A020` | 263 | UnwindData |  |
| 285 | `GL_DrawBuffers` | `0x2A130` | 495 | UnwindData |  |
| 292 | `GL_DrawElementsInstanced` | `0x2A320` | 318 | UnwindData |  |
| 301 | `GL_DrawRangeElements` | `0x2A460` | 335 | UnwindData |  |
| 324 | `GL_EndQuery` | `0x2A5B0` | 279 | UnwindData |  |
| 327 | `GL_EndTransformFeedback` | `0x2A6D0` | 283 | UnwindData |  |
| 328 | `GL_FenceSync` | `0x2A7F0` | 228 | UnwindData |  |
| 332 | `GL_FlushMappedBufferRange` | `0x2A8E0` | 246 | UnwindData |  |
| 358 | `GL_FramebufferTextureLayer` | `0x2A9E0` | 488 | UnwindData |  |
| 372 | `GL_GenQueries` | `0x2ABD0` | 326 | UnwindData |  |
| 376 | `GL_GenSamplers` | `0x2AD20` | 317 | UnwindData |  |
| 379 | `GL_GenTransformFeedbacks` | `0x2AE60` | 326 | UnwindData |  |
| 380 | `GL_GenVertexArrays` | `0x2AFB0` | 339 | UnwindData |  |
| 386 | `GL_GetActiveUniformBlockName` | `0x2B110` | 343 | UnwindData |  |
| 387 | `GL_GetActiveUniformBlockiv` | `0x2B270` | 239 | UnwindData |  |
| 389 | `GL_GetActiveUniformsiv` | `0x2B360` | 260 | UnwindData |  |
| 396 | `GL_GetBufferParameteri64v` | `0x2B470` | 338 | UnwindData |  |
| 400 | `GL_GetBufferPointerv` | `0x2B5D0` | 338 | UnwindData |  |
| 414 | `GL_GetFragDataLocation` | `0x2B730` | 256 | UnwindData |  |
| 429 | `GL_GetInteger64i_v` | `0x2B830` | 414 | UnwindData |  |
| 431 | `GL_GetInteger64v` | `0x2B9D0` | 336 | UnwindData |  |
| 434 | `GL_GetIntegeri_v` | `0x2BB20` | 231 | UnwindData |  |
| 438 | `GL_GetInternalformativ` | `0x2BC10` | 263 | UnwindData |  |
| 463 | `GL_GetProgramBinary` | `0x2BD20` | 262 | UnwindData |  |
| 485 | `GL_GetQueryObjectuiv` | `0x2BE30` | 216 | UnwindData |  |
| 488 | `GL_GetQueryiv` | `0x2BF10` | 326 | UnwindData |  |
| 503 | `GL_GetSamplerParameterfv` | `0x2C060` | 255 | UnwindData |  |
| 505 | `GL_GetSamplerParameteriv` | `0x2C160` | 255 | UnwindData |  |
| 514 | `GL_GetStringi` | `0x2C260` | 194 | UnwindData |  |
| 515 | `GL_GetSynciv` | `0x2C330` | 278 | UnwindData |  |
| 542 | `GL_GetTransformFeedbackVarying` | `0x2C450` | 377 | UnwindData |  |
| 544 | `GL_GetUniformBlockIndex` | `0x2C5D0` | 196 | UnwindData |  |
| 545 | `GL_GetUniformIndices` | `0x2C6A0` | 262 | UnwindData |  |
| 551 | `GL_GetUniformuiv` | `0x2C7B0` | 222 | UnwindData |  |
| 555 | `GL_GetVertexAttribIiv` | `0x2C890` | 236 | UnwindData |  |
| 557 | `GL_GetVertexAttribIuiv` | `0x2C980` | 236 | UnwindData |  |
| 582 | `GL_InvalidateFramebuffer` | `0x2CA70` | 579 | UnwindData |  |
| 583 | `GL_InvalidateSubFramebuffer` | `0x2CCC0` | 759 | UnwindData |  |
| 597 | `GL_IsQuery` | `0x2CFC0` | 154 | UnwindData |  |
| 601 | `GL_IsSampler` | `0x2D060` | 154 | UnwindData |  |
| 604 | `GL_IsSync` | `0x2D100` | 165 | UnwindData |  |
| 606 | `GL_IsTransformFeedback` | `0x2D1B0` | 154 | UnwindData |  |
| 607 | `GL_IsVertexArray` | `0x2D250` | 348 | UnwindData |  |
| 629 | `GL_MapBufferRange` | `0x2D3B0` | 278 | UnwindData |  |
| 670 | `GL_PauseTransformFeedback` | `0x2D4D0` | 318 | UnwindData |  |
| 692 | `GL_ProgramBinary` | `0x2D610` | 234 | UnwindData |  |
| 694 | `GL_ProgramParameteri` | `0x2D700` | 226 | UnwindData |  |
| 769 | `GL_ReadBuffer` | `0x2D7F0` | 226 | UnwindData |  |
| 779 | `GL_RenderbufferStorageMultisample` | `0x2D8E0` | 326 | UnwindData |  |
| 784 | `GL_ResumeTransformFeedback` | `0x2DA30` | 291 | UnwindData |  |
| 799 | `GL_SamplerParameterf` | `0x2DB60` | 376 | UnwindData |  |
| 800 | `GL_SamplerParameterfv` | `0x2DCE0` | 263 | UnwindData |  |
| 802 | `GL_SamplerParameteri` | `0x2DDF0` | 362 | UnwindData |  |
| 803 | `GL_SamplerParameteriv` | `0x2DF60` | 263 | UnwindData |  |
| 848 | `GL_TexImage3D` | `0x2E070` | 594 | UnwindData |  |
| 867 | `GL_TexStorage2D` | `0x2E2D0` | 348 | UnwindData |  |
| 871 | `GL_TexStorage3D` | `0x2E430` | 385 | UnwindData |  |
| 887 | `GL_TexSubImage3D` | `0x2E5C0` | 631 | UnwindData |  |
| 891 | `GL_TransformFeedbackVaryings` | `0x2E840` | 234 | UnwindData |  |
| 898 | `GL_Uniform1ui` | `0x2E930` | 375 | UnwindData |  |
| 899 | `GL_Uniform1uiv` | `0x2EAB0` | 339 | UnwindData |  |
| 904 | `GL_Uniform2ui` | `0x2EC10` | 391 | UnwindData |  |
| 905 | `GL_Uniform2uiv` | `0x2EDA0` | 339 | UnwindData |  |
| 910 | `GL_Uniform3ui` | `0x2EF00` | 402 | UnwindData |  |
| 911 | `GL_Uniform3uiv` | `0x2F0A0` | 339 | UnwindData |  |
| 916 | `GL_Uniform4ui` | `0x2F200` | 422 | UnwindData |  |
| 917 | `GL_Uniform4uiv` | `0x2F3B0` | 339 | UnwindData |  |
| 918 | `GL_UniformBlockBinding` | `0x2F510` | 317 | UnwindData |  |
| 920 | `GL_UniformMatrix2x3fv` | `0x2F650` | 372 | UnwindData |  |
| 921 | `GL_UniformMatrix2x4fv` | `0x2F7D0` | 372 | UnwindData |  |
| 923 | `GL_UniformMatrix3x2fv` | `0x2F950` | 372 | UnwindData |  |
| 924 | `GL_UniformMatrix3x4fv` | `0x2FAD0` | 372 | UnwindData |  |
| 926 | `GL_UniformMatrix4x2fv` | `0x2FC50` | 372 | UnwindData |  |
| 927 | `GL_UniformMatrix4x3fv` | `0x2FDD0` | 372 | UnwindData |  |
| 928 | `GL_UnmapBuffer` | `0x2FF50` | 366 | UnwindData |  |
| 945 | `GL_VertexAttribDivisor` | `0x300C0` | 250 | UnwindData |  |
| 949 | `GL_VertexAttribI4i` | `0x301C0` | 391 | UnwindData |  |
| 950 | `GL_VertexAttribI4iv` | `0x30350` | 227 | UnwindData |  |
| 951 | `GL_VertexAttribI4ui` | `0x30440` | 391 | UnwindData |  |
| 952 | `GL_VertexAttribI4uiv` | `0x305D0` | 227 | UnwindData |  |
| 954 | `GL_VertexAttribIPointer` | `0x306C0` | 544 | UnwindData |  |
| 960 | `GL_WaitSync` | `0x308E0` | 303 | UnwindData |  |
| 117 | `GL_ActiveShaderProgram` | `0x30DB0` | 204 | UnwindData |  |
| 136 | `GL_BindImageTexture` | `0x30E80` | 311 | UnwindData |  |
| 137 | `GL_BindProgramPipeline` | `0x30FC0` | 289 | UnwindData |  |
| 147 | `GL_BindVertexBuffer` | `0x310F0` | 234 | UnwindData |  |
| 232 | `GL_CreateShaderProgramv` | `0x311E0` | 212 | UnwindData |  |
| 249 | `GL_DeleteProgramPipelines` | `0x312C0` | 326 | UnwindData |  |
| 276 | `GL_DispatchCompute` | `0x31410` | 226 | UnwindData |  |
| 277 | `GL_DispatchComputeIndirect` | `0x31500` | 193 | UnwindData |  |
| 279 | `GL_DrawArraysIndirect` | `0x315D0` | 221 | UnwindData |  |
| 291 | `GL_DrawElementsIndirect` | `0x316B0` | 265 | UnwindData |  |
| 342 | `GL_FramebufferParameteri` | `0x317C0` | 516 | UnwindData |  |
| 370 | `GL_GenProgramPipelines` | `0x319D0` | 314 | UnwindData |  |
| 392 | `GL_GetBooleani_v` | `0x31B10` | 414 | UnwindData |  |
| 419 | `GL_GetFramebufferParameteriv` | `0x31CB0` | 344 | UnwindData |  |
| 445 | `GL_GetMultisamplefv` | `0x31E10` | 355 | UnwindData |  |
| 466 | `GL_GetProgramInterfaceiv` | `0x31F80` | 235 | UnwindData |  |
| 468 | `GL_GetProgramPipelineInfoLog` | `0x32070` | 334 | UnwindData |  |
| 470 | `GL_GetProgramPipelineiv` | `0x321C0` | 252 | UnwindData |  |
| 472 | `GL_GetProgramResourceIndex` | `0x322C0` | 257 | UnwindData |  |
| 473 | `GL_GetProgramResourceLocation` | `0x323D0` | 292 | UnwindData |  |
| 475 | `GL_GetProgramResourceName` | `0x32500` | 285 | UnwindData |  |
| 476 | `GL_GetProgramResourceiv` | `0x32620` | 359 | UnwindData |  |
| 523 | `GL_GetTexLevelParameterfv` | `0x32790` | 324 | UnwindData |  |
| 526 | `GL_GetTexLevelParameteriv` | `0x328E0` | 324 | UnwindData |  |
| 595 | `GL_IsProgramPipeline` | `0x32A30` | 170 | UnwindData |  |
| 638 | `GL_MemoryBarrier` | `0x32AE0` | 244 | UnwindData |  |
| 639 | `GL_MemoryBarrierByRegion` | `0x32BE0` | 227 | UnwindData |  |
| 696 | `GL_ProgramUniform1f` | `0x32CD0` | 351 | UnwindData |  |
| 698 | `GL_ProgramUniform1fv` | `0x32E30` | 237 | UnwindData |  |
| 700 | `GL_ProgramUniform1i` | `0x32F20` | 344 | UnwindData |  |
| 702 | `GL_ProgramUniform1iv` | `0x33080` | 235 | UnwindData |  |
| 704 | `GL_ProgramUniform1ui` | `0x33170` | 335 | UnwindData |  |
| 706 | `GL_ProgramUniform1uiv` | `0x332C0` | 237 | UnwindData |  |
| 708 | `GL_ProgramUniform2f` | `0x333B0` | 379 | UnwindData |  |
| 710 | `GL_ProgramUniform2fv` | `0x33530` | 237 | UnwindData |  |
| 712 | `GL_ProgramUniform2i` | `0x33620` | 349 | UnwindData |  |
| 714 | `GL_ProgramUniform2iv` | `0x33780` | 237 | UnwindData |  |
| 716 | `GL_ProgramUniform2ui` | `0x33870` | 349 | UnwindData |  |
| 718 | `GL_ProgramUniform2uiv` | `0x339D0` | 237 | UnwindData |  |
| 720 | `GL_ProgramUniform3f` | `0x33AC0` | 431 | UnwindData |  |
| 722 | `GL_ProgramUniform3fv` | `0x33C70` | 237 | UnwindData |  |
| 724 | `GL_ProgramUniform3i` | `0x33D60` | 369 | UnwindData |  |
| 726 | `GL_ProgramUniform3iv` | `0x33EE0` | 237 | UnwindData |  |
| 728 | `GL_ProgramUniform3ui` | `0x33FD0` | 369 | UnwindData |  |
| 730 | `GL_ProgramUniform3uiv` | `0x34150` | 237 | UnwindData |  |
| 732 | `GL_ProgramUniform4f` | `0x34240` | 483 | UnwindData |  |
| 734 | `GL_ProgramUniform4fv` | `0x34430` | 237 | UnwindData |  |
| 736 | `GL_ProgramUniform4i` | `0x34520` | 389 | UnwindData |  |
| 738 | `GL_ProgramUniform4iv` | `0x346B0` | 237 | UnwindData |  |
| 740 | `GL_ProgramUniform4ui` | `0x347A0` | 389 | UnwindData |  |
| 742 | `GL_ProgramUniform4uiv` | `0x34930` | 237 | UnwindData |  |
| 744 | `GL_ProgramUniformMatrix2fv` | `0x34A20` | 257 | UnwindData |  |
| 746 | `GL_ProgramUniformMatrix2x3fv` | `0x34B30` | 257 | UnwindData |  |
| 748 | `GL_ProgramUniformMatrix2x4fv` | `0x34C40` | 257 | UnwindData |  |
| 750 | `GL_ProgramUniformMatrix3fv` | `0x34D50` | 257 | UnwindData |  |
| 752 | `GL_ProgramUniformMatrix3x2fv` | `0x34E60` | 257 | UnwindData |  |
| 754 | `GL_ProgramUniformMatrix3x4fv` | `0x34F70` | 257 | UnwindData |  |
| 756 | `GL_ProgramUniformMatrix4fv` | `0x35080` | 257 | UnwindData |  |
| 758 | `GL_ProgramUniformMatrix4x2fv` | `0x35190` | 257 | UnwindData |  |
| 760 | `GL_ProgramUniformMatrix4x3fv` | `0x352A0` | 257 | UnwindData |  |
| 789 | `GL_SampleMaski` | `0x353B0` | 208 | UnwindData |  |
| 869 | `GL_TexStorage2DMultisample` | `0x35480` | 372 | UnwindData |  |
| 931 | `GL_UseProgramStages` | `0x35600` | 226 | UnwindData |  |
| 934 | `GL_ValidateProgramPipeline` | `0x356F0` | 221 | UnwindData |  |
| 944 | `GL_VertexAttribBinding` | `0x357D0` | 284 | UnwindData |  |
| 948 | `GL_VertexAttribFormat` | `0x358F0` | 430 | UnwindData |  |
| 953 | `GL_VertexAttribIFormat` | `0x35AA0` | 397 | UnwindData |  |
| 956 | `GL_VertexBindingDivisor` | `0x35C30` | 247 | UnwindData |  |
| 148 | `GL_BlendBarrier` | `0x35D30` | 168 | UnwindData |  |
| 994 | `glBlendBarrier` | `0x35D30` | 168 | UnwindData |  |
| 154 | `GL_BlendEquationSeparatei` | `0x35DE0` | 330 | UnwindData |  |
| 157 | `GL_BlendEquationi` | `0x35F30` | 282 | UnwindData |  |
| 162 | `GL_BlendFuncSeparatei` | `0x36050` | 332 | UnwindData |  |
| 165 | `GL_BlendFunci` | `0x361A0` | 303 | UnwindData |  |
| 200 | `GL_ColorMaski` | `0x362D0` | 287 | UnwindData |  |
| 217 | `GL_CopyImageSubData` | `0x363F0` | 711 | UnwindData |  |
| 236 | `GL_DebugMessageCallback` | `0x366C0` | 170 | UnwindData |  |
| 1082 | `glDebugMessageCallback` | `0x366C0` | 170 | UnwindData |  |
| 238 | `GL_DebugMessageControl` | `0x36770` | 280 | UnwindData |  |
| 240 | `GL_DebugMessageInsert` | `0x36890` | 285 | UnwindData |  |
| 272 | `GL_Disablei` | `0x369B0` | 217 | UnwindData |  |
| 288 | `GL_DrawElementsBaseVertex` | `0x36A90` | 310 | UnwindData |  |
| 295 | `GL_DrawElementsInstancedBaseVertex` | `0x36BD0` | 339 | UnwindData |  |
| 302 | `GL_DrawRangeElementsBaseVertex` | `0x36D30` | 363 | UnwindData |  |
| 319 | `GL_Enablei` | `0x36EA0` | 217 | UnwindData |  |
| 352 | `GL_FramebufferTexture` | `0x36F80` | 462 | UnwindData |  |
| 406 | `GL_GetDebugMessageLog` | `0x37150` | 284 | UnwindData |  |
| 426 | `GL_GetGraphicsResetStatus` | `0x37270` | 153 | UnwindData |  |
| 1272 | `glGetGraphicsResetStatus` | `0x37270` | 153 | UnwindData |  |
| 448 | `GL_GetObjectLabel` | `0x37310` | 285 | UnwindData |  |
| 451 | `GL_GetObjectPtrLabel` | `0x37430` | 276 | UnwindData |  |
| 459 | `GL_GetPointerv` | `0x37550` | 221 | UnwindData |  |
| 495 | `GL_GetSamplerParameterIiv` | `0x37630` | 255 | UnwindData |  |
| 499 | `GL_GetSamplerParameterIuiv` | `0x37730` | 255 | UnwindData |  |
| 529 | `GL_GetTexParameterIiv` | `0x37830` | 298 | UnwindData |  |
| 533 | `GL_GetTexParameterIuiv` | `0x37960` | 298 | UnwindData |  |
| 565 | `GL_GetnUniformfv` | `0x37A90` | 239 | UnwindData |  |
| 569 | `GL_GetnUniformiv` | `0x37B80` | 239 | UnwindData |  |
| 573 | `GL_GetnUniformuiv` | `0x37C70` | 239 | UnwindData |  |
| 587 | `GL_IsEnabledi` | `0x37D60` | 310 | UnwindData |  |
| 641 | `GL_MinSampleShading` | `0x37EA0` | 218 | UnwindData |  |
| 661 | `GL_ObjectLabel` | `0x37F80` | 235 | UnwindData |  |
| 663 | `GL_ObjectPtrLabel` | `0x38070` | 413 | UnwindData |  |
| 667 | `GL_PatchParameteri` | `0x38210` | 229 | UnwindData |  |
| 685 | `GL_PopDebugGroup` | `0x38300` | 262 | UnwindData |  |
| 689 | `GL_PrimitiveBoundingBox` | `0x38410` | 494 | UnwindData |  |
| 1535 | `glPrimitiveBoundingBox` | `0x38410` | 494 | UnwindData |  |
| 763 | `GL_PushDebugGroup` | `0x38600` | 235 | UnwindData |  |
| 772 | `GL_ReadnPixels` | `0x386F0` | 427 | UnwindData |  |
| 791 | `GL_SamplerParameterIiv` | `0x388A0` | 263 | UnwindData |  |
| 795 | `GL_SamplerParameterIuiv` | `0x389B0` | 263 | UnwindData |  |
| 826 | `GL_TexBuffer` | `0x38AC0` | 319 | UnwindData |  |
| 829 | `GL_TexBufferRange` | `0x38C00` | 361 | UnwindData |  |
| 851 | `GL_TexParameterIiv` | `0x38D70` | 307 | UnwindData |  |
| 855 | `GL_TexParameterIuiv` | `0x38EB0` | 307 | UnwindData |  |
| 873 | `GL_TexStorage3DMultisample` | `0x38FF0` | 315 | UnwindData |  |
| 123 | `GL_BeginPerfMonitorAMD` | `0x39130` | 147 | UnwindData |  |
| 969 | `glBeginPerfMonitorAMD` | `0x39130` | 147 | UnwindData |  |
| 247 | `GL_DeletePerfMonitorsAMD` | `0x391D0` | 140 | UnwindData |  |
| 1093 | `glDeletePerfMonitorsAMD` | `0x391D0` | 140 | UnwindData |  |
| 322 | `GL_EndPerfMonitorAMD` | `0x39260` | 172 | UnwindData |  |
| 369 | `GL_GenPerfMonitorsAMD` | `0x39310` | 164 | UnwindData |  |
| 1215 | `glGenPerfMonitorsAMD` | `0x39310` | 164 | UnwindData |  |
| 453 | `GL_GetPerfMonitorCounterDataAMD` | `0x393C0` | 279 | UnwindData |  |
| 454 | `GL_GetPerfMonitorCounterInfoAMD` | `0x394E0` | 313 | UnwindData |  |
| 455 | `GL_GetPerfMonitorCounterStringAMD` | `0x39620` | 360 | UnwindData |  |
| 456 | `GL_GetPerfMonitorCountersAMD` | `0x39790` | 311 | UnwindData |  |
| 457 | `GL_GetPerfMonitorGroupStringAMD` | `0x398D0` | 290 | UnwindData |  |
| 458 | `GL_GetPerfMonitorGroupsAMD` | `0x39A00` | 173 | UnwindData |  |
| 808 | `GL_SelectPerfMonitorCountersAMD` | `0x39AB0` | 140 | UnwindData |  |
| 1654 | `glSelectPerfMonitorCountersAMD` | `0x39AB0` | 140 | UnwindData |  |
| 282 | `GL_DrawArraysInstancedBaseInstanceANGLE` | `0x39B40` | 279 | UnwindData |  |
| 296 | `GL_DrawElementsInstancedBaseVertexBaseInstanceANGLE` | `0x39C60` | 359 | UnwindData |  |
| 649 | `GL_MultiDrawArraysInstancedBaseInstanceANGLE` | `0x39DD0` | 309 | UnwindData |  |
| 655 | `GL_MultiDrawElementsInstancedBaseVertexBaseInstanceANGLE` | `0x39F10` | 412 | UnwindData |  |
| 171 | `GL_BlobCacheCallbacksANGLE` | `0x3A0B0` | 214 | UnwindData |  |
| 460 | `GL_GetPointervANGLE` | `0x3A190` | 208 | UnwindData |  |
| 226 | `GL_CopyTexture3DANGLE` | `0x3A260` | 400 | UnwindData |  |
| 220 | `GL_CopySubTexture3DANGLE` | `0x3A3F0` | 708 | UnwindData |  |
| 169 | `GL_BlitFramebufferANGLE` | `0x3A6C0` | 447 | UnwindData |  |
| 780 | `GL_RenderbufferStorageMultisampleANGLE` | `0x3A880` | 324 | UnwindData |  |
| 522 | `GL_GetTexImageANGLE` | `0x3A9D0` | 266 | UnwindData |  |
| 405 | `GL_GetCompressedTexImageANGLE` | `0x3AAE0` | 274 | UnwindData |  |
| 491 | `GL_GetRenderbufferImageANGLE` | `0x3AC00` | 269 | UnwindData |  |
| 527 | `GL_GetTexLevelParameterivANGLE` | `0x3AD10` | 322 | UnwindData |  |
| 524 | `GL_GetTexLevelParameterfvANGLE` | `0x3AE60` | 322 | UnwindData |  |
| 281 | `GL_DrawArraysInstancedANGLE` | `0x3AFB0` | 278 | UnwindData |  |
| 293 | `GL_DrawElementsInstancedANGLE` | `0x3B0D0` | 337 | UnwindData |  |
| 946 | `GL_VertexAttribDivisorANGLE` | `0x3B230` | 239 | UnwindData |  |
| 626 | `GL_LogicOpANGLE` | `0x3B320` | 222 | UnwindData |  |
| 881 | `GL_TexStorageMemFlags2DANGLE` | `0x3B400` | 398 | UnwindData |  |
| 882 | `GL_TexStorageMemFlags2DMultisampleANGLE` | `0x3B590` | 140 | UnwindData |  |
| 1728 | `glTexStorageMemFlags2DMultisampleANGLE` | `0x3B590` | 140 | UnwindData |  |
| 883 | `GL_TexStorageMemFlags3DANGLE` | `0x3B620` | 140 | UnwindData |  |
| 1729 | `glTexStorageMemFlags3DANGLE` | `0x3B620` | 140 | UnwindData |  |
| 884 | `GL_TexStorageMemFlags3DMultisampleANGLE` | `0x3B6B0` | 140 | UnwindData |  |
| 1730 | `glTexStorageMemFlags3DMultisampleANGLE` | `0x3B6B0` | 140 | UnwindData |  |
| 578 | `GL_ImportMemoryZirconHandleANGLE` | `0x3B740` | 263 | UnwindData |  |
| 645 | `GL_MultiDrawArraysANGLE` | `0x3B850` | 255 | UnwindData |  |
| 648 | `GL_MultiDrawArraysInstancedANGLE` | `0x3B950` | 283 | UnwindData |  |
| 650 | `GL_MultiDrawElementsANGLE` | `0x3BA70` | 309 | UnwindData |  |
| 654 | `GL_MultiDrawElementsInstancedANGLE` | `0x3BBB0` | 335 | UnwindData |  |
| 680 | `GL_PolygonModeANGLE` | `0x3BD00` | 252 | UnwindData |  |
| 762 | `GL_ProvokingVertexANGLE` | `0x3BE00` | 226 | UnwindData |  |
| 783 | `GL_RequestExtensionANGLE` | `0x3BEF0` | 198 | UnwindData |  |
| 270 | `GL_DisableExtensionANGLE` | `0x3BFC0` | 198 | UnwindData |  |
| 395 | `GL_GetBooleanvRobustANGLE` | `0x3C090` | 477 | UnwindData |  |
| 399 | `GL_GetBufferParameterivRobustANGLE` | `0x3C270` | 612 | UnwindData |  |
| 412 | `GL_GetFloatvRobustANGLE` | `0x3C4E0` | 497 | UnwindData |  |
| 418 | `GL_GetFramebufferAttachmentParameterivRobustANGLE` | `0x3C6E0` | 535 | UnwindData |  |
| 437 | `GL_GetIntegervRobustANGLE` | `0x3C900` | 491 | UnwindData |  |
| 478 | `GL_GetProgramivRobustANGLE` | `0x3CAF0` | 457 | UnwindData |  |
| 494 | `GL_GetRenderbufferParameterivRobustANGLE` | `0x3CCC0` | 501 | UnwindData |  |
| 512 | `GL_GetShaderivRobustANGLE` | `0x3CEC0` | 490 | UnwindData |  |
| 538 | `GL_GetTexParameterfvRobustANGLE` | `0x3D0B0` | 564 | UnwindData |  |
| 540 | `GL_GetTexParameterivRobustANGLE` | `0x3D2F0` | 564 | UnwindData |  |
| 548 | `GL_GetUniformfvRobustANGLE` | `0x3D530` | 470 | UnwindData |  |
| 550 | `GL_GetUniformivRobustANGLE` | `0x3D710` | 470 | UnwindData |  |
| 562 | `GL_GetVertexAttribfvRobustANGLE` | `0x3D8F0` | 502 | UnwindData |  |
| 564 | `GL_GetVertexAttribivRobustANGLE` | `0x3DAF0` | 502 | UnwindData |  |
| 560 | `GL_GetVertexAttribPointervRobustANGLE` | `0x3DCF0` | 320 | UnwindData |  |
| 771 | `GL_ReadPixelsRobustANGLE` | `0x3DE30` | 691 | UnwindData |  |
| 847 | `GL_TexImage2DRobustANGLE` | `0x3E0F0` | 416 | UnwindData |  |
| 861 | `GL_TexParameterfvRobustANGLE` | `0x3E290` | 359 | UnwindData |  |
| 864 | `GL_TexParameterivRobustANGLE` | `0x3E400` | 359 | UnwindData |  |
| 886 | `GL_TexSubImage2DRobustANGLE` | `0x3E570` | 418 | UnwindData |  |
| 850 | `GL_TexImage3DRobustANGLE` | `0x3E720` | 437 | UnwindData |  |
| 889 | `GL_TexSubImage3DRobustANGLE` | `0x3E8E0` | 494 | UnwindData |  |
| 207 | `GL_CompressedTexImage2DRobustANGLE` | `0x3EAD0` | 468 | UnwindData |  |
| 212 | `GL_CompressedTexSubImage2DRobustANGLE` | `0x3ECB0` | 494 | UnwindData |  |
| 210 | `GL_CompressedTexImage3DRobustANGLE` | `0x3EEA0` | 416 | UnwindData |  |
| 215 | `GL_CompressedTexSubImage3DRobustANGLE` | `0x3F040` | 494 | UnwindData |  |
| 490 | `GL_GetQueryivRobustANGLE` | `0x3F230` | 357 | UnwindData |  |
| 487 | `GL_GetQueryObjectuivRobustANGLE` | `0x3F3A0` | 242 | UnwindData |  |
| 402 | `GL_GetBufferPointervRobustANGLE` | `0x3F4A0` | 363 | UnwindData |  |
| 435 | `GL_GetIntegeri_vRobustANGLE` | `0x3F610` | 260 | UnwindData |  |
| 439 | `GL_GetInternalformativRobustANGLE` | `0x3F720` | 283 | UnwindData |  |
| 556 | `GL_GetVertexAttribIivRobustANGLE` | `0x3F840` | 260 | UnwindData |  |
| 558 | `GL_GetVertexAttribIuivRobustANGLE` | `0x3F950` | 260 | UnwindData |  |
| 552 | `GL_GetUniformuivRobustANGLE` | `0x3FA60` | 525 | UnwindData |  |
| 388 | `GL_GetActiveUniformBlockivRobustANGLE` | `0x3FC70` | 274 | UnwindData |  |
| 433 | `GL_GetInteger64vRobustANGLE` | `0x3FD90` | 240 | UnwindData |  |
| 430 | `GL_GetInteger64i_vRobustANGLE` | `0x3FE80` | 432 | UnwindData |  |
| 397 | `GL_GetBufferParameteri64vRobustANGLE` | `0x40030` | 374 | UnwindData |  |
| 804 | `GL_SamplerParameterivRobustANGLE` | `0x401B0` | 343 | UnwindData |  |
| 801 | `GL_SamplerParameterfvRobustANGLE` | `0x40310` | 343 | UnwindData |  |
| 506 | `GL_GetSamplerParameterivRobustANGLE` | `0x40470` | 279 | UnwindData |  |
| 504 | `GL_GetSamplerParameterfvRobustANGLE` | `0x40590` | 279 | UnwindData |  |
| 421 | `GL_GetFramebufferParameterivRobustANGLE` | `0x406B0` | 140 | UnwindData |  |
| 1267 | `glGetFramebufferParameterivRobustANGLE` | `0x406B0` | 140 | UnwindData |  |
| 467 | `GL_GetProgramInterfaceivRobustANGLE` | `0x40740` | 140 | UnwindData |  |
| 1313 | `glGetProgramInterfaceivRobustANGLE` | `0x40740` | 140 | UnwindData |  |
| 393 | `GL_GetBooleani_vRobustANGLE` | `0x407D0` | 432 | UnwindData |  |
| 447 | `GL_GetMultisamplefvRobustANGLE` | `0x40980` | 140 | UnwindData |  |
| 1293 | `glGetMultisamplefvRobustANGLE` | `0x40980` | 140 | UnwindData |  |
| 528 | `GL_GetTexLevelParameterivRobustANGLE` | `0x40A10` | 140 | UnwindData |  |
| 1374 | `glGetTexLevelParameterivRobustANGLE` | `0x40A10` | 140 | UnwindData |  |
| 525 | `GL_GetTexLevelParameterfvRobustANGLE` | `0x40AA0` | 140 | UnwindData |  |
| 1371 | `glGetTexLevelParameterfvRobustANGLE` | `0x40AA0` | 140 | UnwindData |  |
| 462 | `GL_GetPointervRobustANGLERobustANGLE` | `0x40B30` | 140 | UnwindData |  |
| 1308 | `glGetPointervRobustANGLERobustANGLE` | `0x40B30` | 140 | UnwindData |  |
| 775 | `GL_ReadnPixelsRobustANGLE` | `0x40BC0` | 691 | UnwindData |  |
| 568 | `GL_GetnUniformfvRobustANGLE` | `0x40E80` | 140 | UnwindData |  |
| 1414 | `glGetnUniformfvRobustANGLE` | `0x40E80` | 140 | UnwindData |  |
| 572 | `GL_GetnUniformivRobustANGLE` | `0x40F10` | 140 | UnwindData |  |
| 1418 | `glGetnUniformivRobustANGLE` | `0x40F10` | 140 | UnwindData |  |
| 575 | `GL_GetnUniformuivRobustANGLE` | `0x40FA0` | 140 | UnwindData |  |
| 1421 | `glGetnUniformuivRobustANGLE` | `0x40FA0` | 140 | UnwindData |  |
| 854 | `GL_TexParameterIivRobustANGLE` | `0x41030` | 140 | UnwindData |  |
| 1700 | `glTexParameterIivRobustANGLE` | `0x41030` | 140 | UnwindData |  |
| 858 | `GL_TexParameterIuivRobustANGLE` | `0x410C0` | 140 | UnwindData |  |
| 1704 | `glTexParameterIuivRobustANGLE` | `0x410C0` | 140 | UnwindData |  |
| 532 | `GL_GetTexParameterIivRobustANGLE` | `0x41150` | 140 | UnwindData |  |
| 1378 | `glGetTexParameterIivRobustANGLE` | `0x41150` | 140 | UnwindData |  |
| 536 | `GL_GetTexParameterIuivRobustANGLE` | `0x411E0` | 140 | UnwindData |  |
| 1382 | `glGetTexParameterIuivRobustANGLE` | `0x411E0` | 140 | UnwindData |  |
| 794 | `GL_SamplerParameterIivRobustANGLE` | `0x41270` | 140 | UnwindData |  |
| 1640 | `glSamplerParameterIivRobustANGLE` | `0x41270` | 140 | UnwindData |  |
| 798 | `GL_SamplerParameterIuivRobustANGLE` | `0x41300` | 140 | UnwindData |  |
| 1644 | `glSamplerParameterIuivRobustANGLE` | `0x41300` | 140 | UnwindData |  |
| 498 | `GL_GetSamplerParameterIivRobustANGLE` | `0x41390` | 140 | UnwindData |  |
| 1344 | `glGetSamplerParameterIivRobustANGLE` | `0x41390` | 140 | UnwindData |  |
| 502 | `GL_GetSamplerParameterIuivRobustANGLE` | `0x41420` | 140 | UnwindData |  |
| 1348 | `glGetSamplerParameterIuivRobustANGLE` | `0x41420` | 140 | UnwindData |  |
| 482 | `GL_GetQueryObjectivRobustANGLE` | `0x414B0` | 242 | UnwindData |  |
| 480 | `GL_GetQueryObjecti64vRobustANGLE` | `0x415B0` | 242 | UnwindData |  |
| 484 | `GL_GetQueryObjectui64vRobustANGLE` | `0x416B0` | 242 | UnwindData |  |
| 423 | `GL_GetFramebufferPixelLocalStorageParameterfvRobustANGLE` | `0x417B0` | 307 | UnwindData |  |
| 425 | `GL_GetFramebufferPixelLocalStorageParameterivRobustANGLE` | `0x418F0` | 307 | UnwindData |  |
| 580 | `GL_ImportSemaphoreZirconHandleANGLE` | `0x41A30` | 327 | UnwindData |  |
| 341 | `GL_FramebufferMemorylessPixelLocalStorageANGLE` | `0x41B80` | 452 | UnwindData |  |
| 361 | `GL_FramebufferTexturePixelLocalStorageANGLE` | `0x41D50` | 460 | UnwindData |  |
| 344 | `GL_FramebufferPixelLocalClearValuefvANGLE` | `0x41F20` | 219 | UnwindData |  |
| 345 | `GL_FramebufferPixelLocalClearValueivANGLE` | `0x42000` | 219 | UnwindData |  |
| 346 | `GL_FramebufferPixelLocalClearValueuivANGLE` | `0x420E0` | 219 | UnwindData |  |
| 124 | `GL_BeginPixelLocalStorageANGLE` | `0x421C0` | 239 | UnwindData |  |
| 323 | `GL_EndPixelLocalStorageANGLE` | `0x422B0` | 249 | UnwindData |  |
| 671 | `GL_PixelLocalStorageBarrierANGLE` | `0x423B0` | 277 | UnwindData |  |
| 347 | `GL_FramebufferPixelLocalStorageInterruptANGLE` | `0x424D0` | 248 | UnwindData |  |
| 348 | `GL_FramebufferPixelLocalStorageRestoreANGLE` | `0x425D0` | 253 | UnwindData |  |
| 422 | `GL_GetFramebufferPixelLocalStorageParameterfvANGLE` | `0x426D0` | 222 | UnwindData |  |
| 424 | `GL_GetFramebufferPixelLocalStorageParameterivANGLE` | `0x427B0` | 222 | UnwindData |  |
| 846 | `GL_TexImage2DExternalANGLE` | `0x42890` | 378 | UnwindData |  |
| 584 | `GL_InvalidateTextureANGLE` | `0x42A10` | 218 | UnwindData |  |
| 870 | `GL_TexStorage2DMultisampleANGLE` | `0x42AF0` | 370 | UnwindData |  |
| 446 | `GL_GetMultisamplefvANGLE` | `0x42C70` | 353 | UnwindData |  |
| 790 | `GL_SampleMaskiANGLE` | `0x42DE0` | 206 | UnwindData |  |
| 543 | `GL_GetTranslatedShaderSourceANGLE` | `0x42EB0` | 289 | UnwindData |  |
| 116 | `GL_AcquireTexturesANGLE` | `0x42FE0` | 226 | UnwindData |  |
| 777 | `GL_ReleaseTexturesANGLE` | `0x430D0` | 226 | UnwindData |  |
| 144 | `GL_BindUniformLocationCHROMIUM` | `0x431C0` | 225 | UnwindData |  |
| 205 | `GL_CompressedCopyTextureCHROMIUM` | `0x432B0` | 202 | UnwindData |  |
| 227 | `GL_CopyTextureCHROMIUM` | `0x43380` | 400 | UnwindData |  |
| 221 | `GL_CopySubTextureCHROMIUM` | `0x43510` | 581 | UnwindData |  |
| 228 | `GL_CoverageModulationCHROMIUM` | `0x43760` | 209 | UnwindData |  |
| 627 | `GL_LoseContextCHROMIUM` | `0x43840` | 411 | UnwindData |  |
| 314 | `GL_EGLImageTargetTexStorageEXT` | `0x43A00` | 329 | UnwindData |  |
| 283 | `GL_DrawArraysInstancedBaseInstanceEXT` | `0x43B50` | 279 | UnwindData |  |
| 294 | `GL_DrawElementsInstancedBaseInstanceEXT` | `0x43C70` | 342 | UnwindData |  |
| 297 | `GL_DrawElementsInstancedBaseVertexBaseInstanceEXT` | `0x43DD0` | 359 | UnwindData |  |
| 132 | `GL_BindFragDataLocationEXT` | `0x43F40` | 286 | UnwindData |  |
| 133 | `GL_BindFragDataLocationIndexedEXT` | `0x44060` | 233 | UnwindData |  |
| 413 | `GL_GetFragDataIndexEXT` | `0x44150` | 243 | UnwindData |  |
| 474 | `GL_GetProgramResourceLocationIndexEXT` | `0x44250` | 214 | UnwindData |  |
| 173 | `GL_BufferStorageEXT` | `0x44330` | 361 | UnwindData |  |
| 189 | `GL_ClearTexImageEXT` | `0x444A0` | 364 | UnwindData |  |
| 190 | `GL_ClearTexSubImageEXT` | `0x44610` | 630 | UnwindData |  |
| 193 | `GL_ClipControlEXT` | `0x44890` | 311 | UnwindData |  |
| 218 | `GL_CopyImageSubDataEXT` | `0x449D0` | 709 | UnwindData |  |
| 449 | `GL_GetObjectLabelEXT` | `0x44CA0` | 283 | UnwindData |  |
| 609 | `GL_LabelObjectEXT` | `0x44DC0` | 262 | UnwindData |  |
| 581 | `GL_InsertEventMarkerEXT` | `0x44ED0` | 241 | UnwindData |  |
| 687 | `GL_PopGroupMarkerEXT` | `0x44FD0` | 166 | UnwindData |  |
| 1533 | `glPopGroupMarkerEXT` | `0x44FD0` | 166 | UnwindData |  |
| 765 | `GL_PushGroupMarkerEXT` | `0x45080` | 274 | UnwindData |  |
| 275 | `GL_DiscardFramebufferEXT` | `0x451A0` | 557 | UnwindData |  |
| 126 | `GL_BeginQueryEXT` | `0x453D0` | 288 | UnwindData |  |
| 252 | `GL_DeleteQueriesEXT` | `0x454F0` | 224 | UnwindData |  |
| 325 | `GL_EndQueryEXT` | `0x455D0` | 286 | UnwindData |  |
| 373 | `GL_GenQueriesEXT` | `0x456F0` | 351 | UnwindData |  |
| 432 | `GL_GetInteger64vEXT` | `0x45850` | 334 | UnwindData |  |
| 479 | `GL_GetQueryObjecti64vEXT` | `0x459A0` | 214 | UnwindData |  |
| 481 | `GL_GetQueryObjectivEXT` | `0x45A80` | 214 | UnwindData |  |
| 483 | `GL_GetQueryObjectui64vEXT` | `0x45B60` | 214 | UnwindData |  |
| 486 | `GL_GetQueryObjectuivEXT` | `0x45C40` | 224 | UnwindData |  |
| 489 | `GL_GetQueryivEXT` | `0x45D20` | 333 | UnwindData |  |
| 598 | `GL_IsQueryEXT` | `0x45E70` | 161 | UnwindData |  |
| 767 | `GL_QueryCounterEXT` | `0x45F20` | 235 | UnwindData |  |
| 286 | `GL_DrawBuffersEXT` | `0x46010` | 271 | UnwindData |  |
| 155 | `GL_BlendEquationSeparateiEXT` | `0x46120` | 307 | UnwindData |  |
| 158 | `GL_BlendEquationiEXT` | `0x46260` | 280 | UnwindData |  |
| 163 | `GL_BlendFuncSeparateiEXT` | `0x46380` | 330 | UnwindData |  |
| 166 | `GL_BlendFunciEXT` | `0x464D0` | 301 | UnwindData |  |
| 201 | `GL_ColorMaskiEXT` | `0x46600` | 285 | UnwindData |  |
| 273 | `GL_DisableiEXT` | `0x46720` | 215 | UnwindData |  |
| 320 | `GL_EnableiEXT` | `0x46800` | 215 | UnwindData |  |
| 588 | `GL_IsEnablediEXT` | `0x468E0` | 308 | UnwindData |  |
| 289 | `GL_DrawElementsBaseVertexEXT` | `0x46A20` | 308 | UnwindData |  |
| 298 | `GL_DrawElementsInstancedBaseVertexEXT` | `0x46B60` | 395 | UnwindData |  |
| 303 | `GL_DrawRangeElementsBaseVertexEXT` | `0x46CF0` | 361 | UnwindData |  |
| 651 | `GL_MultiDrawElementsBaseVertexEXT` | `0x46E60` | 174 | UnwindData |  |
| 284 | `GL_DrawArraysInstancedEXT` | `0x46F10` | 271 | UnwindData |  |
| 300 | `GL_DrawElementsInstancedEXT` | `0x47020` | 325 | UnwindData |  |
| 174 | `GL_BufferStorageExternalEXT` | `0x47170` | 430 | UnwindData |  |
| 351 | `GL_FramebufferShadingRateEXT` | `0x47320` | 140 | UnwindData |  |
| 1197 | `glFramebufferShadingRateEXT` | `0x47320` | 140 | UnwindData |  |
| 415 | `GL_GetFragmentShadingRatesEXT` | `0x473B0` | 218 | UnwindData |  |
| 815 | `GL_ShadingRateEXT` | `0x47490` | 239 | UnwindData |  |
| 814 | `GL_ShadingRateCombinerOpsEXT` | `0x47580` | 247 | UnwindData |  |
| 357 | `GL_FramebufferTextureEXT` | `0x47680` | 460 | UnwindData |  |
| 947 | `GL_VertexAttribDivisorEXT` | `0x47850` | 248 | UnwindData |  |
| 333 | `GL_FlushMappedBufferRangeEXT` | `0x47950` | 244 | UnwindData |  |
| 630 | `GL_MapBufferRangeEXT` | `0x47A50` | 276 | UnwindData |  |
| 175 | `GL_BufferStorageMemEXT` | `0x47B70` | 140 | UnwindData |  |
| 1021 | `glBufferStorageMemEXT` | `0x47B70` | 140 | UnwindData |  |
| 229 | `GL_CreateMemoryObjectsEXT` | `0x47C00` | 388 | UnwindData |  |
| 246 | `GL_DeleteMemoryObjectsEXT` | `0x47D90` | 251 | UnwindData |  |
| 444 | `GL_GetMemoryObjectParameterivEXT` | `0x47E90` | 248 | UnwindData |  |
| 554 | `GL_GetUnsignedBytevEXT` | `0x47F90` | 149 | UnwindData |  |
| 1400 | `glGetUnsignedBytevEXT` | `0x47F90` | 149 | UnwindData |  |
| 553 | `GL_GetUnsignedBytei_vEXT` | `0x48030` | 149 | UnwindData |  |
| 1399 | `glGetUnsignedBytei_vEXT` | `0x48030` | 149 | UnwindData |  |
| 593 | `GL_IsMemoryObjectEXT` | `0x480D0` | 168 | UnwindData |  |
| 640 | `GL_MemoryObjectParameterivEXT` | `0x48180` | 284 | UnwindData |  |
| 877 | `GL_TexStorageMem2DEXT` | `0x482A0` | 429 | UnwindData |  |
| 878 | `GL_TexStorageMem2DMultisampleEXT` | `0x48450` | 140 | UnwindData |  |
| 1724 | `glTexStorageMem2DMultisampleEXT` | `0x48450` | 140 | UnwindData |  |
| 879 | `GL_TexStorageMem3DEXT` | `0x484E0` | 140 | UnwindData |  |
| 1725 | `glTexStorageMem3DEXT` | `0x484E0` | 140 | UnwindData |  |
| 880 | `GL_TexStorageMem3DMultisampleEXT` | `0x48570` | 140 | UnwindData |  |
| 1726 | `glTexStorageMem3DMultisampleEXT` | `0x48570` | 140 | UnwindData |  |
| 577 | `GL_ImportMemoryFdEXT` | `0x48600` | 263 | UnwindData |  |
| 646 | `GL_MultiDrawArraysEXT` | `0x48710` | 194 | UnwindData |  |
| 652 | `GL_MultiDrawElementsEXT` | `0x487E0` | 234 | UnwindData |  |
| 647 | `GL_MultiDrawArraysIndirectEXT` | `0x488D0` | 304 | UnwindData |  |
| 653 | `GL_MultiDrawElementsIndirectEXT` | `0x48A00` | 307 | UnwindData |  |
| 354 | `GL_FramebufferTexture2DMultisampleEXT` | `0x48B40` | 565 | UnwindData |  |
| 781 | `GL_RenderbufferStorageMultisampleEXT` | `0x48D80` | 324 | UnwindData |  |
| 683 | `GL_PolygonOffsetClampEXT` | `0x48ED0` | 281 | UnwindData |  |
| 690 | `GL_PrimitiveBoundingBoxEXT` | `0x48FF0` | 492 | UnwindData |  |
| 1536 | `glPrimitiveBoundingBoxEXT` | `0x48FF0` | 492 | UnwindData |  |
| 427 | `GL_GetGraphicsResetStatusEXT` | `0x491E0` | 151 | UnwindData |  |
| 1273 | `glGetGraphicsResetStatusEXT` | `0x491E0` | 151 | UnwindData |  |
| 566 | `GL_GetnUniformfvEXT` | `0x49280` | 237 | UnwindData |  |
| 570 | `GL_GetnUniformivEXT` | `0x49370` | 237 | UnwindData |  |
| 773 | `GL_ReadnPixelsEXT` | `0x49460` | 425 | UnwindData |  |
| 256 | `GL_DeleteSemaphoresEXT` | `0x49610` | 251 | UnwindData |  |
| 377 | `GL_GenSemaphoresEXT` | `0x49710` | 388 | UnwindData |  |
| 507 | `GL_GetSemaphoreParameterui64vEXT` | `0x498A0` | 140 | UnwindData |  |
| 1353 | `glGetSemaphoreParameterui64vEXT` | `0x498A0` | 140 | UnwindData |  |
| 602 | `GL_IsSemaphoreEXT` | `0x49930` | 168 | UnwindData |  |
| 809 | `GL_SemaphoreParameterui64vEXT` | `0x499E0` | 140 | UnwindData |  |
| 1655 | `glSemaphoreParameterui64vEXT` | `0x499E0` | 140 | UnwindData |  |
| 817 | `GL_SignalSemaphoreEXT` | `0x49A70` | 284 | UnwindData |  |
| 959 | `GL_WaitSemaphoreEXT` | `0x49B90` | 284 | UnwindData |  |
| 579 | `GL_ImportSemaphoreFdEXT` | `0x49CB0` | 280 | UnwindData |  |
| 118 | `GL_ActiveShaderProgramEXT` | `0x49DD0` | 202 | UnwindData |  |
| 138 | `GL_BindProgramPipelineEXT` | `0x49EA0` | 287 | UnwindData |  |
| 233 | `GL_CreateShaderProgramvEXT` | `0x49FC0` | 215 | UnwindData |  |
| 250 | `GL_DeleteProgramPipelinesEXT` | `0x4A0A0` | 320 | UnwindData |  |
| 371 | `GL_GenProgramPipelinesEXT` | `0x4A1E0` | 312 | UnwindData |  |
| 469 | `GL_GetProgramPipelineInfoLogEXT` | `0x4A320` | 332 | UnwindData |  |
| 471 | `GL_GetProgramPipelineivEXT` | `0x4A470` | 255 | UnwindData |  |
| 596 | `GL_IsProgramPipelineEXT` | `0x4A570` | 168 | UnwindData |  |
| 695 | `GL_ProgramParameteriEXT` | `0x4A620` | 224 | UnwindData |  |
| 697 | `GL_ProgramUniform1fEXT` | `0x4A700` | 345 | UnwindData |  |
| 699 | `GL_ProgramUniform1fvEXT` | `0x4A860` | 235 | UnwindData |  |
| 701 | `GL_ProgramUniform1iEXT` | `0x4A950` | 342 | UnwindData |  |
| 703 | `GL_ProgramUniform1ivEXT` | `0x4AAB0` | 233 | UnwindData |  |
| 705 | `GL_ProgramUniform1uiEXT` | `0x4ABA0` | 333 | UnwindData |  |
| 707 | `GL_ProgramUniform1uivEXT` | `0x4ACF0` | 235 | UnwindData |  |
| 709 | `GL_ProgramUniform2fEXT` | `0x4ADE0` | 377 | UnwindData |  |
| 711 | `GL_ProgramUniform2fvEXT` | `0x4AF60` | 235 | UnwindData |  |
| 713 | `GL_ProgramUniform2iEXT` | `0x4B050` | 347 | UnwindData |  |
| 715 | `GL_ProgramUniform2ivEXT` | `0x4B1B0` | 235 | UnwindData |  |
| 717 | `GL_ProgramUniform2uiEXT` | `0x4B2A0` | 347 | UnwindData |  |
| 719 | `GL_ProgramUniform2uivEXT` | `0x4B400` | 235 | UnwindData |  |
| 721 | `GL_ProgramUniform3fEXT` | `0x4B4F0` | 429 | UnwindData |  |
| 723 | `GL_ProgramUniform3fvEXT` | `0x4B6A0` | 235 | UnwindData |  |
| 725 | `GL_ProgramUniform3iEXT` | `0x4B790` | 367 | UnwindData |  |
| 727 | `GL_ProgramUniform3ivEXT` | `0x4B900` | 235 | UnwindData |  |
| 729 | `GL_ProgramUniform3uiEXT` | `0x4B9F0` | 367 | UnwindData |  |
| 731 | `GL_ProgramUniform3uivEXT` | `0x4BB60` | 235 | UnwindData |  |
| 733 | `GL_ProgramUniform4fEXT` | `0x4BC50` | 481 | UnwindData |  |
| 735 | `GL_ProgramUniform4fvEXT` | `0x4BE40` | 235 | UnwindData |  |
| 737 | `GL_ProgramUniform4iEXT` | `0x4BF30` | 387 | UnwindData |  |
| 739 | `GL_ProgramUniform4ivEXT` | `0x4C0C0` | 235 | UnwindData |  |
| 741 | `GL_ProgramUniform4uiEXT` | `0x4C1B0` | 387 | UnwindData |  |
| 743 | `GL_ProgramUniform4uivEXT` | `0x4C340` | 235 | UnwindData |  |
| 745 | `GL_ProgramUniformMatrix2fvEXT` | `0x4C430` | 255 | UnwindData |  |
| 747 | `GL_ProgramUniformMatrix2x3fvEXT` | `0x4C530` | 255 | UnwindData |  |
| 749 | `GL_ProgramUniformMatrix2x4fvEXT` | `0x4C630` | 255 | UnwindData |  |
| 751 | `GL_ProgramUniformMatrix3fvEXT` | `0x4C730` | 255 | UnwindData |  |
| 753 | `GL_ProgramUniformMatrix3x2fvEXT` | `0x4C830` | 255 | UnwindData |  |
| 755 | `GL_ProgramUniformMatrix3x4fvEXT` | `0x4C930` | 255 | UnwindData |  |
| 757 | `GL_ProgramUniformMatrix4fvEXT` | `0x4CA30` | 255 | UnwindData |  |
| 759 | `GL_ProgramUniformMatrix4x2fvEXT` | `0x4CB30` | 255 | UnwindData |  |
| 761 | `GL_ProgramUniformMatrix4x3fvEXT` | `0x4CC30` | 255 | UnwindData |  |
| 932 | `GL_UseProgramStagesEXT` | `0x4CD30` | 224 | UnwindData |  |
| 935 | `GL_ValidateProgramPipelineEXT` | `0x4CE10` | 219 | UnwindData |  |
| 338 | `GL_FramebufferFetchBarrierEXT` | `0x4CEF0` | 166 | UnwindData |  |
| 1184 | `glFramebufferFetchBarrierEXT` | `0x4CEF0` | 166 | UnwindData |  |
| 668 | `GL_PatchParameteriEXT` | `0x4CFA0` | 227 | UnwindData |  |
| 496 | `GL_GetSamplerParameterIivEXT` | `0x4D090` | 285 | UnwindData |  |
| 500 | `GL_GetSamplerParameterIuivEXT` | `0x4D1B0` | 285 | UnwindData |  |
| 530 | `GL_GetTexParameterIivEXT` | `0x4D2D0` | 331 | UnwindData |  |
| 534 | `GL_GetTexParameterIuivEXT` | `0x4D420` | 331 | UnwindData |  |
| 792 | `GL_SamplerParameterIivEXT` | `0x4D570` | 293 | UnwindData |  |
| 796 | `GL_SamplerParameterIuivEXT` | `0x4D6A0` | 293 | UnwindData |  |
| 852 | `GL_TexParameterIivEXT` | `0x4D7D0` | 340 | UnwindData |  |
| 856 | `GL_TexParameterIuivEXT` | `0x4D930` | 340 | UnwindData |  |
| 827 | `GL_TexBufferEXT` | `0x4DA90` | 317 | UnwindData |  |
| 830 | `GL_TexBufferRangeEXT` | `0x4DBD0` | 359 | UnwindData |  |
| 868 | `GL_TexStorage2DEXT` | `0x4DD40` | 266 | UnwindData |  |
| 872 | `GL_TexStorage3DEXT` | `0x4DE50` | 376 | UnwindData |  |
| 875 | `GL_TexStorageAttribs2DEXT` | `0x4DFD0` | 283 | UnwindData |  |
| 876 | `GL_TexStorageAttribs3DEXT` | `0x4E0F0` | 309 | UnwindData |  |
| 149 | `GL_BlendBarrierKHR` | `0x4E230` | 166 | UnwindData |  |
| 995 | `glBlendBarrierKHR` | `0x4E230` | 166 | UnwindData |  |
| 237 | `GL_DebugMessageCallbackKHR` | `0x4E2E0` | 168 | UnwindData |  |
| 1083 | `glDebugMessageCallbackKHR` | `0x4E2E0` | 168 | UnwindData |  |
| 239 | `GL_DebugMessageControlKHR` | `0x4E390` | 278 | UnwindData |  |
| 241 | `GL_DebugMessageInsertKHR` | `0x4E4B0` | 279 | UnwindData |  |
| 407 | `GL_GetDebugMessageLogKHR` | `0x4E5D0` | 282 | UnwindData |  |
| 450 | `GL_GetObjectLabelKHR` | `0x4E6F0` | 283 | UnwindData |  |
| 452 | `GL_GetObjectPtrLabelKHR` | `0x4E810` | 274 | UnwindData |  |
| 461 | `GL_GetPointervKHR` | `0x4E930` | 208 | UnwindData |  |
| 662 | `GL_ObjectLabelKHR` | `0x4EA00` | 306 | UnwindData |  |
| 664 | `GL_ObjectPtrLabelKHR` | `0x4EB40` | 514 | UnwindData |  |
| 686 | `GL_PopDebugGroupKHR` | `0x4ED50` | 260 | UnwindData |  |
| 764 | `GL_PushDebugGroupKHR` | `0x4EE60` | 230 | UnwindData |  |
| 637 | `GL_MaxShaderCompilerThreadsKHR` | `0x4EF50` | 152 | UnwindData |  |
| 1483 | `glMaxShaderCompilerThreadsKHR` | `0x4EF50` | 152 | UnwindData |  |
| 428 | `GL_GetGraphicsResetStatusKHR` | `0x4EFF0` | 178 | UnwindData |  |
| 567 | `GL_GetnUniformfvKHR` | `0x4F0B0` | 269 | UnwindData |  |
| 571 | `GL_GetnUniformivKHR` | `0x4F1C0` | 269 | UnwindData |  |
| 574 | `GL_GetnUniformuivKHR` | `0x4F2D0` | 269 | UnwindData |  |
| 774 | `GL_ReadnPixelsKHR` | `0x4F3E0` | 467 | UnwindData |  |
| 343 | `GL_FramebufferParameteriMESA` | `0x4F5C0` | 587 | UnwindData |  |
| 420 | `GL_GetFramebufferParameterivMESA` | `0x4F810` | 381 | UnwindData |  |
| 243 | `GL_DeleteFencesNV` | `0x4F990` | 193 | UnwindData |  |
| 330 | `GL_FinishFenceNV` | `0x4FA60` | 259 | UnwindData |  |
| 366 | `GL_GenFencesNV` | `0x4FB70` | 376 | UnwindData |  |
| 409 | `GL_GetFenceivNV` | `0x4FCF0` | 285 | UnwindData |  |
| 590 | `GL_IsFenceNV` | `0x4FE10` | 152 | UnwindData |  |
| 810 | `GL_SetFenceNV` | `0x4FEB0` | 244 | UnwindData |  |
| 825 | `GL_TestFenceNV` | `0x4FFB0` | 207 | UnwindData |  |
| 170 | `GL_BlitFramebufferNV` | `0x50080` | 447 | UnwindData |  |
| 681 | `GL_PolygonModeNV` | `0x50240` | 268 | UnwindData |  |
| 313 | `GL_EGLImageTargetRenderbufferStorageOES` | `0x50350` | 329 | UnwindData |  |
| 315 | `GL_EGLImageTargetTexture2DOES` | `0x504A0` | 422 | UnwindData |  |
| 152 | `GL_BlendEquationOES` | `0x50650` | 307 | UnwindData |  |
| 219 | `GL_CopyImageSubDataOES` | `0x50790` | 709 | UnwindData |  |
| 156 | `GL_BlendEquationSeparateiOES` | `0x50A60` | 307 | UnwindData |  |
| 159 | `GL_BlendEquationiOES` | `0x50BA0` | 280 | UnwindData |  |
| 164 | `GL_BlendFuncSeparateiOES` | `0x50CC0` | 330 | UnwindData |  |
| 167 | `GL_BlendFunciOES` | `0x50E10` | 301 | UnwindData |  |
| 202 | `GL_ColorMaskiOES` | `0x50F40` | 285 | UnwindData |  |
| 274 | `GL_DisableiOES` | `0x51060` | 215 | UnwindData |  |
| 321 | `GL_EnableiOES` | `0x51140` | 215 | UnwindData |  |
| 589 | `GL_IsEnablediOES` | `0x51220` | 308 | UnwindData |  |
| 290 | `GL_DrawElementsBaseVertexOES` | `0x51360` | 308 | UnwindData |  |
| 299 | `GL_DrawElementsInstancedBaseVertexOES` | `0x514A0` | 395 | UnwindData |  |
| 304 | `GL_DrawRangeElementsBaseVertexOES` | `0x51630` | 361 | UnwindData |  |
| 305 | `GL_DrawTexfOES` | `0x517A0` | 424 | UnwindData |  |
| 306 | `GL_DrawTexfvOES` | `0x51950` | 285 | UnwindData |  |
| 307 | `GL_DrawTexiOES` | `0x51A70` | 309 | UnwindData |  |
| 308 | `GL_DrawTexivOES` | `0x51BB0` | 289 | UnwindData |  |
| 309 | `GL_DrawTexsOES` | `0x51CE0` | 327 | UnwindData |  |
| 310 | `GL_DrawTexsvOES` | `0x51E30` | 312 | UnwindData |  |
| 311 | `GL_DrawTexxOES` | `0x51F70` | 375 | UnwindData |  |
| 312 | `GL_DrawTexxvOES` | `0x520F0` | 344 | UnwindData |  |
| 135 | `GL_BindFramebufferOES` | `0x52250` | 202 | UnwindData |  |
| 140 | `GL_BindRenderbufferOES` | `0x52320` | 254 | UnwindData |  |
| 178 | `GL_CheckFramebufferStatusOES` | `0x52420` | 333 | UnwindData |  |
| 245 | `GL_DeleteFramebuffersOES` | `0x52570` | 252 | UnwindData |  |
| 254 | `GL_DeleteRenderbuffersOES` | `0x52670` | 316 | UnwindData |  |
| 350 | `GL_FramebufferRenderbufferOES` | `0x527B0` | 231 | UnwindData |  |
| 355 | `GL_FramebufferTexture2DOES` | `0x528A0` | 496 | UnwindData |  |
| 368 | `GL_GenFramebuffersOES` | `0x52A90` | 312 | UnwindData |  |
| 375 | `GL_GenRenderbuffersOES` | `0x52BD0` | 312 | UnwindData |  |
| 383 | `GL_GenerateMipmapOES` | `0x52D10` | 262 | UnwindData |  |
| 417 | `GL_GetFramebufferAttachmentParameterivOES` | `0x52E20` | 288 | UnwindData |  |
| 493 | `GL_GetRenderbufferParameterivOES` | `0x52F40` | 234 | UnwindData |  |
| 592 | `GL_IsFramebufferOES` | `0x53030` | 168 | UnwindData |  |
| 600 | `GL_IsRenderbufferOES` | `0x530E0` | 168 | UnwindData |  |
| 782 | `GL_RenderbufferStorageOES` | `0x53190` | 294 | UnwindData |  |
| 360 | `GL_FramebufferTextureOES` | `0x532C0` | 460 | UnwindData |  |
| 464 | `GL_GetProgramBinaryOES` | `0x53490` | 260 | UnwindData |  |
| 693 | `GL_ProgramBinaryOES` | `0x535A0` | 232 | UnwindData |  |
| 401 | `GL_GetBufferPointervOES` | `0x53690` | 336 | UnwindData |  |
| 628 | `GL_MapBufferOES` | `0x537E0` | 312 | UnwindData |  |
| 929 | `GL_UnmapBufferOES` | `0x53920` | 364 | UnwindData |  |
| 235 | `GL_CurrentPaletteMatrixOES` | `0x53A90` | 140 | UnwindData |  |
| 1081 | `glCurrentPaletteMatrixOES` | `0x53A90` | 140 | UnwindData |  |
| 624 | `GL_LoadPaletteFromModelViewMatrixOES` | `0x53B20` | 140 | UnwindData |  |
| 1470 | `glLoadPaletteFromModelViewMatrixOES` | `0x53B20` | 140 | UnwindData |  |
| 635 | `GL_MatrixIndexPointerOES` | `0x53BB0` | 140 | UnwindData |  |
| 1481 | `glMatrixIndexPointerOES` | `0x53BB0` | 140 | UnwindData |  |
| 961 | `GL_WeightPointerOES` | `0x53C40` | 140 | UnwindData |  |
| 1807 | `glWeightPointerOES` | `0x53C40` | 140 | UnwindData |  |
| 678 | `GL_PointSizePointerOES` | `0x53CD0` | 517 | UnwindData |  |
| 691 | `GL_PrimitiveBoundingBoxOES` | `0x53EE0` | 492 | UnwindData |  |
| 1537 | `glPrimitiveBoundingBoxOES` | `0x53EE0` | 492 | UnwindData |  |
| 768 | `GL_QueryMatrixxOES` | `0x540D0` | 138 | UnwindData |  |
| 1614 | `glQueryMatrixxOES` | `0x540D0` | 138 | UnwindData |  |
| 642 | `GL_MinSampleShadingOES` | `0x54160` | 216 | UnwindData |  |
| 669 | `GL_PatchParameteriOES` | `0x54240` | 227 | UnwindData |  |
| 209 | `GL_CompressedTexImage3DOES` | `0x54330` | 402 | UnwindData |  |
| 214 | `GL_CompressedTexSubImage3DOES` | `0x544D0` | 475 | UnwindData |  |
| 225 | `GL_CopyTexSubImage3DOES` | `0x546B0` | 825 | UnwindData |  |
| 356 | `GL_FramebufferTexture3DOES` | `0x549F0` | 565 | UnwindData |  |
| 849 | `GL_TexImage3DOES` | `0x54C30` | 611 | UnwindData |  |
| 888 | `GL_TexSubImage3DOES` | `0x54EA0` | 652 | UnwindData |  |
| 497 | `GL_GetSamplerParameterIivOES` | `0x55130` | 285 | UnwindData |  |
| 501 | `GL_GetSamplerParameterIuivOES` | `0x55250` | 285 | UnwindData |  |
| 531 | `GL_GetTexParameterIivOES` | `0x55370` | 331 | UnwindData |  |
| 535 | `GL_GetTexParameterIuivOES` | `0x554C0` | 331 | UnwindData |  |
| 793 | `GL_SamplerParameterIivOES` | `0x55610` | 293 | UnwindData |  |
| 797 | `GL_SamplerParameterIuivOES` | `0x55740` | 293 | UnwindData |  |
| 853 | `GL_TexParameterIivOES` | `0x55870` | 340 | UnwindData |  |
| 857 | `GL_TexParameterIuivOES` | `0x559D0` | 340 | UnwindData |  |
| 828 | `GL_TexBufferOES` | `0x55B30` | 317 | UnwindData |  |
| 831 | `GL_TexBufferRangeOES` | `0x55C70` | 359 | UnwindData |  |
| 519 | `GL_GetTexGenfvOES` | `0x55DE0` | 140 | UnwindData |  |
| 1365 | `glGetTexGenfvOES` | `0x55DE0` | 140 | UnwindData |  |
| 520 | `GL_GetTexGenivOES` | `0x55E70` | 140 | UnwindData |  |
| 1366 | `glGetTexGenivOES` | `0x55E70` | 140 | UnwindData |  |
| 521 | `GL_GetTexGenxvOES` | `0x55F00` | 140 | UnwindData |  |
| 1367 | `glGetTexGenxvOES` | `0x55F00` | 140 | UnwindData |  |
| 839 | `GL_TexGenfOES` | `0x55F90` | 140 | UnwindData |  |
| 1685 | `glTexGenfOES` | `0x55F90` | 140 | UnwindData |  |
| 840 | `GL_TexGenfvOES` | `0x56020` | 140 | UnwindData |  |
| 1686 | `glTexGenfvOES` | `0x56020` | 140 | UnwindData |  |
| 841 | `GL_TexGeniOES` | `0x560B0` | 140 | UnwindData |  |
| 1687 | `glTexGeniOES` | `0x560B0` | 140 | UnwindData |  |
| 842 | `GL_TexGenivOES` | `0x56140` | 140 | UnwindData |  |
| 1688 | `glTexGenivOES` | `0x56140` | 140 | UnwindData |  |
| 843 | `GL_TexGenxOES` | `0x561D0` | 140 | UnwindData |  |
| 1689 | `glTexGenxOES` | `0x561D0` | 140 | UnwindData |  |
| 844 | `GL_TexGenxvOES` | `0x56260` | 140 | UnwindData |  |
| 1690 | `glTexGenxvOES` | `0x56260` | 140 | UnwindData |  |
| 874 | `GL_TexStorage3DMultisampleOES` | `0x562F0` | 313 | UnwindData |  |
| 146 | `GL_BindVertexArrayOES` | `0x56430` | 251 | UnwindData |  |
| 262 | `GL_DeleteVertexArraysOES` | `0x56530` | 213 | UnwindData |  |
| 381 | `GL_GenVertexArraysOES` | `0x56610` | 337 | UnwindData |  |
| 608 | `GL_IsVertexArrayOES` | `0x56770` | 346 | UnwindData |  |
| 359 | `GL_FramebufferTextureMultiviewOVR` | `0x568D0` | 543 | UnwindData |  |
| 339 | `GL_FramebufferFoveationConfigQCOM` | `0x56AF0` | 344 | UnwindData |  |
| 340 | `GL_FramebufferFoveationParametersQCOM` | `0x56C50` | 487 | UnwindData |  |
| 816 | `GL_ShadingRateQCOM` | `0x56E40` | 227 | UnwindData |  |
| 890 | `GL_TextureFoveationParametersQCOM` | `0x56F30` | 479 | UnwindData |  |
| 326 | `GL_EndTilingQCOM` | `0x57110` | 165 | UnwindData |  |
| 818 | `GL_StartTilingQCOM` | `0x571C0` | 486 | UnwindData |  |
| 965 | `glActiveTexture` | `0x57490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 968 | `glAttachShader` | `0x574A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 974 | `glBindAttribLocation` | `0x574B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `glBindBuffer` | `0x574C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `glBindFramebuffer` | `0x574D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `glBindRenderbuffer` | `0x574E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `glBindTexture` | `0x574F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `glBlendColor` | `0x57500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 997 | `glBlendEquation` | `0x57510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `glBlendEquationSeparate` | `0x57520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `glBlendFunc` | `0x57530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `glBlendFuncSeparate` | `0x57540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `glBufferData` | `0x57550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `glBufferSubData` | `0x57560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `glCheckFramebufferStatus` | `0x57570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1050 | `glCompileShader` | `0x57580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `glCompressedTexImage2D` | `0x57590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `glCompressedTexSubImage2D` | `0x575A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1068 | `glCopyTexImage2D` | `0x575B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1069 | `glCopyTexSubImage2D` | `0x575C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `glCreateProgram` | `0x575D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1077 | `glCreateShader` | `0x575E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1080 | `glCullFace` | `0x575F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1088 | `glDeleteBuffers` | `0x57600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `glDeleteFramebuffers` | `0x57610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `glDeleteProgram` | `0x57620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1099 | `glDeleteRenderbuffers` | `0x57630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1103 | `glDeleteShader` | `0x57640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `glDeleteTextures` | `0x57650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1109 | `glDepthFunc` | `0x57660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1111 | `glDepthRangef` | `0x57670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1113 | `glDetachShader` | `0x57680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1114 | `glDisable` | `0x57690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1117 | `glDisableVertexAttribArray` | `0x576A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `glDrawArrays` | `0x576B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1133 | `glDrawElements` | `0x576C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1162 | `glEnable` | `0x576D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1164 | `glEnableVertexAttribArray` | `0x576E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `glFramebufferRenderbuffer` | `0x576F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `glFramebufferTexture2D` | `0x57700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `glFrontFace` | `0x57710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `glGenBuffers` | `0x57720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `glGenFramebuffers` | `0x57730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `glGenRenderbuffers` | `0x57740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1224 | `glGenTextures` | `0x57750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1228 | `glGenerateMipmap` | `0x57760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `glGetActiveAttrib` | `0x57770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `glGetActiveUniform` | `0x57780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1236 | `glGetAttachedShaders` | `0x57790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1237 | `glGetAttribLocation` | `0x577A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1240 | `glGetBooleanv` | `0x577B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1244 | `glGetBufferParameteriv` | `0x577C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `glGetFloatv` | `0x577D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1262 | `glGetFramebufferAttachmentParameteriv` | `0x577E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1282 | `glGetIntegerv` | `0x577F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `glGetProgramInfoLog` | `0x57800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `glGetProgramiv` | `0x57810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `glGetRenderbufferParameteriv` | `0x57820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1354 | `glGetShaderInfoLog` | `0x57830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `glGetShaderPrecisionFormat` | `0x57840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1356 | `glGetShaderSource` | `0x57850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1357 | `glGetShaderiv` | `0x57860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1359 | `glGetString` | `0x57870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1383 | `glGetTexParameterfv` | `0x57880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1385 | `glGetTexParameteriv` | `0x57890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1392 | `glGetUniformLocation` | `0x578A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1393 | `glGetUniformfv` | `0x578B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1395 | `glGetUniformiv` | `0x578C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1405 | `glGetVertexAttribPointerv` | `0x578D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `glGetVertexAttribfv` | `0x578E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1409 | `glGetVertexAttribiv` | `0x578F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1422 | `glHint` | `0x57900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1432 | `glIsEnabled` | `0x57910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1437 | `glIsFramebuffer` | `0x57920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1440 | `glIsProgram` | `0x57930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1445 | `glIsRenderbuffer` | `0x57940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1449 | `glIsShader` | `0x57950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1466 | `glLinkProgram` | `0x57960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1518 | `glPixelStorei` | `0x57970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1616 | `glReadPixels` | `0x57980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1622 | `glReleaseShaderCompiler` | `0x57990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1624 | `glRenderbufferStorage` | `0x579A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1653 | `glScissor` | `0x579B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1658 | `glShaderBinary` | `0x579C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1659 | `glShaderSource` | `0x579D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1665 | `glStencilFunc` | `0x579E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1666 | `glStencilFuncSeparate` | `0x579F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `glStencilMaskSeparate` | `0x57A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1669 | `glStencilOp` | `0x57A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1670 | `glStencilOpSeparate` | `0x57A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1691 | `glTexImage2D` | `0x57A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1705 | `glTexParameterf` | `0x57A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1706 | `glTexParameterfv` | `0x57A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1708 | `glTexParameteri` | `0x57A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1709 | `glTexParameteriv` | `0x57A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1731 | `glTexSubImage2D` | `0x57A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1740 | `glUniform1f` | `0x57A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1741 | `glUniform1fv` | `0x57AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1742 | `glUniform1i` | `0x57AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1743 | `glUniform1iv` | `0x57AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1746 | `glUniform2f` | `0x57AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1747 | `glUniform2fv` | `0x57AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1748 | `glUniform2i` | `0x57AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1749 | `glUniform2iv` | `0x57B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1752 | `glUniform3f` | `0x57B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1753 | `glUniform3fv` | `0x57B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1754 | `glUniform3i` | `0x57B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1755 | `glUniform3iv` | `0x57B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1758 | `glUniform4f` | `0x57B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1759 | `glUniform4fv` | `0x57B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1760 | `glUniform4i` | `0x57B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1761 | `glUniform4iv` | `0x57B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1765 | `glUniformMatrix2fv` | `0x57B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1768 | `glUniformMatrix3fv` | `0x57BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1771 | `glUniformMatrix4fv` | `0x57BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1776 | `glUseProgram` | `0x57BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1779 | `glValidateProgram` | `0x57BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1782 | `glVertexAttrib1f` | `0x57BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1783 | `glVertexAttrib1fv` | `0x57BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1784 | `glVertexAttrib2f` | `0x57C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1785 | `glVertexAttrib2fv` | `0x57C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1786 | `glVertexAttrib3f` | `0x57C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1787 | `glVertexAttrib3fv` | `0x57C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1788 | `glVertexAttrib4f` | `0x57C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1789 | `glVertexAttrib4fv` | `0x57C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1801 | `glVertexAttribPointer` | `0x57C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1804 | `glViewport` | `0x57C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 971 | `glBeginQuery` | `0x57C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `glBeginTransformFeedback` | `0x57C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `glBindBufferBase` | `0x57CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `glBindBufferRange` | `0x57CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 987 | `glBindSampler` | `0x57CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `glBindTransformFeedback` | `0x57CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `glBindVertexArray` | `0x57CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `glBlitFramebuffer` | `0x57CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `glClearBufferfi` | `0x57D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `glClearBufferfv` | `0x57D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1028 | `glClearBufferiv` | `0x57D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1029 | `glClearBufferuiv` | `0x57D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `glClientWaitSync` | `0x57D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `glCompressedTexImage3D` | `0x57D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `glCompressedTexSubImage3D` | `0x57D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1062 | `glCopyBufferSubData` | `0x57D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1070 | `glCopyTexSubImage3D` | `0x57D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `glDeleteQueries` | `0x57D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `glDeleteSamplers` | `0x57DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `glDeleteSync` | `0x57DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `glDeleteTransformFeedbacks` | `0x57DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `glDeleteVertexArrays` | `0x57DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1126 | `glDrawArraysInstanced` | `0x57DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1131 | `glDrawBuffers` | `0x57DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `glDrawElementsInstanced` | `0x57E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1147 | `glDrawRangeElements` | `0x57E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1170 | `glEndQuery` | `0x57E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `glEndTransformFeedback` | `0x57E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `glFenceSync` | `0x57E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `glFlushMappedBufferRange` | `0x57E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1204 | `glFramebufferTextureLayer` | `0x57E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1218 | `glGenQueries` | `0x57E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1222 | `glGenSamplers` | `0x57E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `glGenTransformFeedbacks` | `0x57E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `glGenVertexArrays` | `0x57EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `glGetActiveUniformBlockName` | `0x57EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1233 | `glGetActiveUniformBlockiv` | `0x57EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1235 | `glGetActiveUniformsiv` | `0x57ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1242 | `glGetBufferParameteri64v` | `0x57EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1246 | `glGetBufferPointerv` | `0x57EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1260 | `glGetFragDataLocation` | `0x57F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1275 | `glGetInteger64i_v` | `0x57F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1277 | `glGetInteger64v` | `0x57F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1280 | `glGetIntegeri_v` | `0x57F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `glGetInternalformativ` | `0x57F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1309 | `glGetProgramBinary` | `0x57F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `glGetQueryObjectuiv` | `0x57F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `glGetQueryiv` | `0x57F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1349 | `glGetSamplerParameterfv` | `0x57F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1351 | `glGetSamplerParameteriv` | `0x57F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1360 | `glGetStringi` | `0x57FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1361 | `glGetSynciv` | `0x57FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1388 | `glGetTransformFeedbackVarying` | `0x57FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1390 | `glGetUniformBlockIndex` | `0x57FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1391 | `glGetUniformIndices` | `0x57FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1397 | `glGetUniformuiv` | `0x57FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1401 | `glGetVertexAttribIiv` | `0x58000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1403 | `glGetVertexAttribIuiv` | `0x58010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1428 | `glInvalidateFramebuffer` | `0x58020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1429 | `glInvalidateSubFramebuffer` | `0x58030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1443 | `glIsQuery` | `0x58040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1447 | `glIsSampler` | `0x58050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1450 | `glIsSync` | `0x58060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1452 | `glIsTransformFeedback` | `0x58070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1453 | `glIsVertexArray` | `0x58080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1475 | `glMapBufferRange` | `0x58090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1516 | `glPauseTransformFeedback` | `0x580A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `glProgramBinary` | `0x580B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1540 | `glProgramParameteri` | `0x580C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1615 | `glReadBuffer` | `0x580D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1625 | `glRenderbufferStorageMultisample` | `0x580E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `glResumeTransformFeedback` | `0x580F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1645 | `glSamplerParameterf` | `0x58100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1646 | `glSamplerParameterfv` | `0x58110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1648 | `glSamplerParameteri` | `0x58120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1649 | `glSamplerParameteriv` | `0x58130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1694 | `glTexImage3D` | `0x58140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1713 | `glTexStorage2D` | `0x58150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1717 | `glTexStorage3D` | `0x58160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1733 | `glTexSubImage3D` | `0x58170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `glTransformFeedbackVaryings` | `0x58180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1744 | `glUniform1ui` | `0x58190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1745 | `glUniform1uiv` | `0x581A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1750 | `glUniform2ui` | `0x581B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1751 | `glUniform2uiv` | `0x581C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1756 | `glUniform3ui` | `0x581D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1757 | `glUniform3uiv` | `0x581E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1762 | `glUniform4ui` | `0x581F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1763 | `glUniform4uiv` | `0x58200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1764 | `glUniformBlockBinding` | `0x58210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1766 | `glUniformMatrix2x3fv` | `0x58220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1767 | `glUniformMatrix2x4fv` | `0x58230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1769 | `glUniformMatrix3x2fv` | `0x58240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1770 | `glUniformMatrix3x4fv` | `0x58250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1772 | `glUniformMatrix4x2fv` | `0x58260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1773 | `glUniformMatrix4x3fv` | `0x58270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1774 | `glUnmapBuffer` | `0x58280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1791 | `glVertexAttribDivisor` | `0x58290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1795 | `glVertexAttribI4i` | `0x582A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1796 | `glVertexAttribI4iv` | `0x582B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1797 | `glVertexAttribI4ui` | `0x582C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1798 | `glVertexAttribI4uiv` | `0x582D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1800 | `glVertexAttribIPointer` | `0x582E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1806 | `glWaitSync` | `0x582F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 963 | `glActiveShaderProgram` | `0x58300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 982 | `glBindImageTexture` | `0x58310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 983 | `glBindProgramPipeline` | `0x58320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `glBindVertexBuffer` | `0x58330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `glCreateShaderProgramv` | `0x58340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `glDeleteProgramPipelines` | `0x58350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `glDispatchCompute` | `0x58360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1123 | `glDispatchComputeIndirect` | `0x58370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1125 | `glDrawArraysIndirect` | `0x58380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `glDrawElementsIndirect` | `0x58390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1188 | `glFramebufferParameteri` | `0x583A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1216 | `glGenProgramPipelines` | `0x583B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1238 | `glGetBooleani_v` | `0x583C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1265 | `glGetFramebufferParameteriv` | `0x583D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1291 | `glGetMultisamplefv` | `0x583E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1312 | `glGetProgramInterfaceiv` | `0x583F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1314 | `glGetProgramPipelineInfoLog` | `0x58400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1316 | `glGetProgramPipelineiv` | `0x58410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1318 | `glGetProgramResourceIndex` | `0x58420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `glGetProgramResourceLocation` | `0x58430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `glGetProgramResourceName` | `0x58440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1322 | `glGetProgramResourceiv` | `0x58450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1369 | `glGetTexLevelParameterfv` | `0x58460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1372 | `glGetTexLevelParameteriv` | `0x58470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1441 | `glIsProgramPipeline` | `0x58480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1484 | `glMemoryBarrier` | `0x58490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1485 | `glMemoryBarrierByRegion` | `0x584A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1542 | `glProgramUniform1f` | `0x584B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1544 | `glProgramUniform1fv` | `0x584C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1546 | `glProgramUniform1i` | `0x584D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1548 | `glProgramUniform1iv` | `0x584E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1550 | `glProgramUniform1ui` | `0x584F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1552 | `glProgramUniform1uiv` | `0x58500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1554 | `glProgramUniform2f` | `0x58510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1556 | `glProgramUniform2fv` | `0x58520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1558 | `glProgramUniform2i` | `0x58530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1560 | `glProgramUniform2iv` | `0x58540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1562 | `glProgramUniform2ui` | `0x58550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1564 | `glProgramUniform2uiv` | `0x58560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1566 | `glProgramUniform3f` | `0x58570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1568 | `glProgramUniform3fv` | `0x58580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `glProgramUniform3i` | `0x58590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1572 | `glProgramUniform3iv` | `0x585A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1574 | `glProgramUniform3ui` | `0x585B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1576 | `glProgramUniform3uiv` | `0x585C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `glProgramUniform4f` | `0x585D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1580 | `glProgramUniform4fv` | `0x585E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1582 | `glProgramUniform4i` | `0x585F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1584 | `glProgramUniform4iv` | `0x58600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1586 | `glProgramUniform4ui` | `0x58610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `glProgramUniform4uiv` | `0x58620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1590 | `glProgramUniformMatrix2fv` | `0x58630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1592 | `glProgramUniformMatrix2x3fv` | `0x58640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1594 | `glProgramUniformMatrix2x4fv` | `0x58650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1596 | `glProgramUniformMatrix3fv` | `0x58660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1598 | `glProgramUniformMatrix3x2fv` | `0x58670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1600 | `glProgramUniformMatrix3x4fv` | `0x58680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1602 | `glProgramUniformMatrix4fv` | `0x58690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1604 | `glProgramUniformMatrix4x2fv` | `0x586A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1606 | `glProgramUniformMatrix4x3fv` | `0x586B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1635 | `glSampleMaski` | `0x586C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1715 | `glTexStorage2DMultisample` | `0x586D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1777 | `glUseProgramStages` | `0x586E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1780 | `glValidateProgramPipeline` | `0x586F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1790 | `glVertexAttribBinding` | `0x58700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1794 | `glVertexAttribFormat` | `0x58710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1799 | `glVertexAttribIFormat` | `0x58720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1802 | `glVertexBindingDivisor` | `0x58730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `glBlendEquationSeparatei` | `0x58740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `glBlendEquationi` | `0x58750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1008 | `glBlendFuncSeparatei` | `0x58760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `glBlendFunci` | `0x58770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1046 | `glColorMaski` | `0x58780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1063 | `glCopyImageSubData` | `0x58790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1084 | `glDebugMessageControl` | `0x587A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1086 | `glDebugMessageInsert` | `0x587B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1118 | `glDisablei` | `0x587C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1134 | `glDrawElementsBaseVertex` | `0x587D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1141 | `glDrawElementsInstancedBaseVertex` | `0x587E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1148 | `glDrawRangeElementsBaseVertex` | `0x587F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1165 | `glEnablei` | `0x58800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `glFramebufferTexture` | `0x58810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1252 | `glGetDebugMessageLog` | `0x58820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1294 | `glGetObjectLabel` | `0x58830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1297 | `glGetObjectPtrLabel` | `0x58840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1305 | `glGetPointerv` | `0x58850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1341 | `glGetSamplerParameterIiv` | `0x58860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1345 | `glGetSamplerParameterIuiv` | `0x58870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1375 | `glGetTexParameterIiv` | `0x58880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1379 | `glGetTexParameterIuiv` | `0x58890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1411 | `glGetnUniformfv` | `0x588A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1415 | `glGetnUniformiv` | `0x588B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1419 | `glGetnUniformuiv` | `0x588C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1433 | `glIsEnabledi` | `0x588D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1487 | `glMinSampleShading` | `0x588E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1507 | `glObjectLabel` | `0x588F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1509 | `glObjectPtrLabel` | `0x58900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1513 | `glPatchParameteri` | `0x58910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `glPopDebugGroup` | `0x58920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1609 | `glPushDebugGroup` | `0x58930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1618 | `glReadnPixels` | `0x58940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1637 | `glSamplerParameterIiv` | `0x58950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1641 | `glSamplerParameterIuiv` | `0x58960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1672 | `glTexBuffer` | `0x58970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1675 | `glTexBufferRange` | `0x58980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1697 | `glTexParameterIiv` | `0x58990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1701 | `glTexParameterIuiv` | `0x589A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1719 | `glTexStorage3DMultisample` | `0x589B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 966 | `glAlphaFunc` | `0x589C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 967 | `glAlphaFuncx` | `0x589D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1031 | `glClearColorx` | `0x589E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1033 | `glClearDepthx` | `0x589F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `glClientActiveTexture` | `0x58A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1040 | `glClipPlanef` | `0x58A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | `glClipPlanex` | `0x58A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1042 | `glColor4f` | `0x58A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1043 | `glColor4ub` | `0x58A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1044 | `glColor4x` | `0x58A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1049 | `glColorPointer` | `0x58A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1112 | `glDepthRangex` | `0x58A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1115 | `glDisableClientState` | `0x58A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1163 | `glEnableClientState` | `0x58A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `glFogf` | `0x58AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `glFogfv` | `0x58AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1182 | `glFogx` | `0x58AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `glFogxv` | `0x58AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `glFrustumf` | `0x58AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `glFrustumx` | `0x58AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `glGetClipPlanef` | `0x58B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1250 | `glGetClipPlanex` | `0x58B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1256 | `glGetFixedv` | `0x58B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1286 | `glGetLightfv` | `0x58B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `glGetLightxv` | `0x58B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1288 | `glGetMaterialfv` | `0x58B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `glGetMaterialxv` | `0x58B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1362 | `glGetTexEnvfv` | `0x58B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1363 | `glGetTexEnviv` | `0x58B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1364 | `glGetTexEnvxv` | `0x58B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `glGetTexParameterxv` | `0x58BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1456 | `glLightModelf` | `0x58BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1457 | `glLightModelfv` | `0x58BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1458 | `glLightModelx` | `0x58BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1459 | `glLightModelxv` | `0x58BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1460 | `glLightf` | `0x58BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1461 | `glLightfv` | `0x58C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1462 | `glLightx` | `0x58C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1463 | `glLightxv` | `0x58C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1465 | `glLineWidthx` | `0x58C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1467 | `glLoadIdentity` | `0x58C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1468 | `glLoadMatrixf` | `0x58C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1469 | `glLoadMatrixx` | `0x58C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1471 | `glLogicOp` | `0x58C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1477 | `glMaterialf` | `0x58C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1478 | `glMaterialfv` | `0x58C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `glMaterialx` | `0x58CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1480 | `glMaterialxv` | `0x58CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1482 | `glMatrixMode` | `0x58CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1489 | `glMultMatrixf` | `0x58CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1490 | `glMultMatrixx` | `0x58CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `glMultiTexCoord4f` | `0x58CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1503 | `glMultiTexCoord4x` | `0x58D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1504 | `glNormal3f` | `0x58D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `glNormal3x` | `0x58D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1506 | `glNormalPointer` | `0x58D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1511 | `glOrthof` | `0x58D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `glOrthox` | `0x58D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `glPointParameterf` | `0x58D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1520 | `glPointParameterfv` | `0x58D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1521 | `glPointParameterx` | `0x58D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `glPointParameterxv` | `0x58D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1523 | `glPointSize` | `0x58DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1525 | `glPointSizex` | `0x58DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1530 | `glPolygonOffsetx` | `0x58DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1534 | `glPopMatrix` | `0x58DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1612 | `glPushMatrix` | `0x58DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1631 | `glRotatef` | `0x58DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1632 | `glRotatex` | `0x58E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1634 | `glSampleCoveragex` | `0x58E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1651 | `glScalef` | `0x58E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1652 | `glScalex` | `0x58E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1657 | `glShadeModel` | `0x58E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1678 | `glTexCoordPointer` | `0x58E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1679 | `glTexEnvf` | `0x58E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1680 | `glTexEnvfv` | `0x58E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1681 | `glTexEnvi` | `0x58E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1682 | `glTexEnviv` | `0x58E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1683 | `glTexEnvx` | `0x58EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1684 | `glTexEnvxv` | `0x58EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1711 | `glTexParameterx` | `0x58EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1712 | `glTexParameterxv` | `0x58ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1738 | `glTranslatef` | `0x58EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `glTranslatex` | `0x58EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1803 | `glVertexPointer` | `0x58F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1168 | `glEndPerfMonitorAMD` | `0x58F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `glGetPerfMonitorCounterDataAMD` | `0x58F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1300 | `glGetPerfMonitorCounterInfoAMD` | `0x58F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1301 | `glGetPerfMonitorCounterStringAMD` | `0x58F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `glGetPerfMonitorCountersAMD` | `0x58F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `glGetPerfMonitorGroupStringAMD` | `0x58F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `glGetPerfMonitorGroupsAMD` | `0x58F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `glDrawArraysInstancedBaseInstanceANGLE` | `0x58F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `glDrawElementsInstancedBaseVertexBaseInstanceANGLE` | `0x58F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1495 | `glMultiDrawArraysInstancedBaseInstanceANGLE` | `0x58FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1501 | `glMultiDrawElementsInstancedBaseVertexBaseInstanceANGLE` | `0x58FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `glBlobCacheCallbacksANGLE` | `0x58FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1306 | `glGetPointervANGLE` | `0x58FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `glCopyTexture3DANGLE` | `0x58FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `glCopySubTexture3DANGLE` | `0x58FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `glBlitFramebufferANGLE` | `0x59000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1626 | `glRenderbufferStorageMultisampleANGLE` | `0x59010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1368 | `glGetTexImageANGLE` | `0x59020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1251 | `glGetCompressedTexImageANGLE` | `0x59030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `glGetRenderbufferImageANGLE` | `0x59040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1373 | `glGetTexLevelParameterivANGLE` | `0x59050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1370 | `glGetTexLevelParameterfvANGLE` | `0x59060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1127 | `glDrawArraysInstancedANGLE` | `0x59070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1139 | `glDrawElementsInstancedANGLE` | `0x59080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1792 | `glVertexAttribDivisorANGLE` | `0x59090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1472 | `glLogicOpANGLE` | `0x590A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1727 | `glTexStorageMemFlags2DANGLE` | `0x590B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1424 | `glImportMemoryZirconHandleANGLE` | `0x590C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1491 | `glMultiDrawArraysANGLE` | `0x590D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1494 | `glMultiDrawArraysInstancedANGLE` | `0x590E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1496 | `glMultiDrawElementsANGLE` | `0x590F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1500 | `glMultiDrawElementsInstancedANGLE` | `0x59100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1526 | `glPolygonModeANGLE` | `0x59110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1608 | `glProvokingVertexANGLE` | `0x59120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1629 | `glRequestExtensionANGLE` | `0x59130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1116 | `glDisableExtensionANGLE` | `0x59140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1241 | `glGetBooleanvRobustANGLE` | `0x59150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1245 | `glGetBufferParameterivRobustANGLE` | `0x59160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `glGetFloatvRobustANGLE` | `0x59170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1264 | `glGetFramebufferAttachmentParameterivRobustANGLE` | `0x59180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1283 | `glGetIntegervRobustANGLE` | `0x59190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1324 | `glGetProgramivRobustANGLE` | `0x591A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1340 | `glGetRenderbufferParameterivRobustANGLE` | `0x591B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1358 | `glGetShaderivRobustANGLE` | `0x591C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `glGetTexParameterfvRobustANGLE` | `0x591D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1386 | `glGetTexParameterivRobustANGLE` | `0x591E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1394 | `glGetUniformfvRobustANGLE` | `0x591F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1396 | `glGetUniformivRobustANGLE` | `0x59200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `glGetVertexAttribfvRobustANGLE` | `0x59210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1410 | `glGetVertexAttribivRobustANGLE` | `0x59220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1406 | `glGetVertexAttribPointervRobustANGLE` | `0x59230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `glReadPixelsRobustANGLE` | `0x59240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1693 | `glTexImage2DRobustANGLE` | `0x59250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1707 | `glTexParameterfvRobustANGLE` | `0x59260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1710 | `glTexParameterivRobustANGLE` | `0x59270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1732 | `glTexSubImage2DRobustANGLE` | `0x59280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1696 | `glTexImage3DRobustANGLE` | `0x59290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1735 | `glTexSubImage3DRobustANGLE` | `0x592A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1053 | `glCompressedTexImage2DRobustANGLE` | `0x592B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `glCompressedTexSubImage2DRobustANGLE` | `0x592C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `glCompressedTexImage3DRobustANGLE` | `0x592D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `glCompressedTexSubImage3DRobustANGLE` | `0x592E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1336 | `glGetQueryivRobustANGLE` | `0x592F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1333 | `glGetQueryObjectuivRobustANGLE` | `0x59300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `glGetBufferPointervRobustANGLE` | `0x59310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1281 | `glGetIntegeri_vRobustANGLE` | `0x59320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `glGetInternalformativRobustANGLE` | `0x59330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `glGetVertexAttribIivRobustANGLE` | `0x59340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1404 | `glGetVertexAttribIuivRobustANGLE` | `0x59350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1398 | `glGetUniformuivRobustANGLE` | `0x59360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `glGetActiveUniformBlockivRobustANGLE` | `0x59370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1279 | `glGetInteger64vRobustANGLE` | `0x59380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1276 | `glGetInteger64i_vRobustANGLE` | `0x59390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1243 | `glGetBufferParameteri64vRobustANGLE` | `0x593A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1650 | `glSamplerParameterivRobustANGLE` | `0x593B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1647 | `glSamplerParameterfvRobustANGLE` | `0x593C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1352 | `glGetSamplerParameterivRobustANGLE` | `0x593D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1350 | `glGetSamplerParameterfvRobustANGLE` | `0x593E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1239 | `glGetBooleani_vRobustANGLE` | `0x593F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `glReadnPixelsRobustANGLE` | `0x59400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `glGetQueryObjectivRobustANGLE` | `0x59410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `glGetQueryObjecti64vRobustANGLE` | `0x59420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `glGetQueryObjectui64vRobustANGLE` | `0x59430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1269 | `glGetFramebufferPixelLocalStorageParameterfvRobustANGLE` | `0x59440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1271 | `glGetFramebufferPixelLocalStorageParameterivRobustANGLE` | `0x59450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1426 | `glImportSemaphoreZirconHandleANGLE` | `0x59460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `glFramebufferMemorylessPixelLocalStorageANGLE` | `0x59470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `glFramebufferTexturePixelLocalStorageANGLE` | `0x59480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `glFramebufferPixelLocalClearValuefvANGLE` | `0x59490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `glFramebufferPixelLocalClearValueivANGLE` | `0x594A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1192 | `glFramebufferPixelLocalClearValueuivANGLE` | `0x594B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 970 | `glBeginPixelLocalStorageANGLE` | `0x594C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1169 | `glEndPixelLocalStorageANGLE` | `0x594D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1517 | `glPixelLocalStorageBarrierANGLE` | `0x594E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `glFramebufferPixelLocalStorageInterruptANGLE` | `0x594F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `glFramebufferPixelLocalStorageRestoreANGLE` | `0x59500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1268 | `glGetFramebufferPixelLocalStorageParameterfvANGLE` | `0x59510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1270 | `glGetFramebufferPixelLocalStorageParameterivANGLE` | `0x59520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1692 | `glTexImage2DExternalANGLE` | `0x59530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `glInvalidateTextureANGLE` | `0x59540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1716 | `glTexStorage2DMultisampleANGLE` | `0x59550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1292 | `glGetMultisamplefvANGLE` | `0x59560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1636 | `glSampleMaskiANGLE` | `0x59570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1389 | `glGetTranslatedShaderSourceANGLE` | `0x59580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 962 | `glAcquireTexturesANGLE` | `0x59590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1623 | `glReleaseTexturesANGLE` | `0x595A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `glBindUniformLocationCHROMIUM` | `0x595B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1051 | `glCompressedCopyTextureCHROMIUM` | `0x595C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `glCopyTextureCHROMIUM` | `0x595D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `glCopySubTextureCHROMIUM` | `0x595E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `glCoverageModulationCHROMIUM` | `0x595F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1473 | `glLoseContextCHROMIUM` | `0x59600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1160 | `glEGLImageTargetTexStorageEXT` | `0x59610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1129 | `glDrawArraysInstancedBaseInstanceEXT` | `0x59620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1140 | `glDrawElementsInstancedBaseInstanceEXT` | `0x59630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `glDrawElementsInstancedBaseVertexBaseInstanceEXT` | `0x59640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `glBindFragDataLocationEXT` | `0x59650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 979 | `glBindFragDataLocationIndexedEXT` | `0x59660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1259 | `glGetFragDataIndexEXT` | `0x59670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `glGetProgramResourceLocationIndexEXT` | `0x59680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `glBufferStorageEXT` | `0x59690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `glClearTexImageEXT` | `0x596A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `glClearTexSubImageEXT` | `0x596B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `glClipControlEXT` | `0x596C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1064 | `glCopyImageSubDataEXT` | `0x596D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1295 | `glGetObjectLabelEXT` | `0x596E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1455 | `glLabelObjectEXT` | `0x596F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1427 | `glInsertEventMarkerEXT` | `0x59700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1611 | `glPushGroupMarkerEXT` | `0x59710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1121 | `glDiscardFramebufferEXT` | `0x59720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `glBeginQueryEXT` | `0x59730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1098 | `glDeleteQueriesEXT` | `0x59740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `glEndQueryEXT` | `0x59750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1219 | `glGenQueriesEXT` | `0x59760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `glGetInteger64vEXT` | `0x59770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1325 | `glGetQueryObjecti64vEXT` | `0x59780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1327 | `glGetQueryObjectivEXT` | `0x59790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1329 | `glGetQueryObjectui64vEXT` | `0x597A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `glGetQueryObjectuivEXT` | `0x597B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1335 | `glGetQueryivEXT` | `0x597C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `glIsQueryEXT` | `0x597D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1613 | `glQueryCounterEXT` | `0x597E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1132 | `glDrawBuffersEXT` | `0x597F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `glBlendEquationSeparateiEXT` | `0x59800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `glBlendEquationiEXT` | `0x59810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `glBlendFuncSeparateiEXT` | `0x59820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `glBlendFunciEXT` | `0x59830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1047 | `glColorMaskiEXT` | `0x59840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1119 | `glDisableiEXT` | `0x59850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1166 | `glEnableiEXT` | `0x59860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1434 | `glIsEnablediEXT` | `0x59870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `glDrawElementsBaseVertexEXT` | `0x59880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `glDrawElementsInstancedBaseVertexEXT` | `0x59890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `glDrawRangeElementsBaseVertexEXT` | `0x598A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1497 | `glMultiDrawElementsBaseVertexEXT` | `0x598B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1130 | `glDrawArraysInstancedEXT` | `0x598C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `glDrawElementsInstancedEXT` | `0x598D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `glBufferStorageExternalEXT` | `0x598E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `glGetFragmentShadingRatesEXT` | `0x598F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1661 | `glShadingRateEXT` | `0x59900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1660 | `glShadingRateCombinerOpsEXT` | `0x59910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `glFramebufferTextureEXT` | `0x59920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1793 | `glVertexAttribDivisorEXT` | `0x59930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1179 | `glFlushMappedBufferRangeEXT` | `0x59940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1476 | `glMapBufferRangeEXT` | `0x59950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1075 | `glCreateMemoryObjectsEXT` | `0x59960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `glDeleteMemoryObjectsEXT` | `0x59970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `glGetMemoryObjectParameterivEXT` | `0x59980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1439 | `glIsMemoryObjectEXT` | `0x59990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1486 | `glMemoryObjectParameterivEXT` | `0x599A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1723 | `glTexStorageMem2DEXT` | `0x599B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1423 | `glImportMemoryFdEXT` | `0x599C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1492 | `glMultiDrawArraysEXT` | `0x599D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1498 | `glMultiDrawElementsEXT` | `0x599E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1493 | `glMultiDrawArraysIndirectEXT` | `0x599F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1499 | `glMultiDrawElementsIndirectEXT` | `0x59A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1200 | `glFramebufferTexture2DMultisampleEXT` | `0x59A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1627 | `glRenderbufferStorageMultisampleEXT` | `0x59A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `glPolygonOffsetClampEXT` | `0x59A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1412 | `glGetnUniformfvEXT` | `0x59A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1416 | `glGetnUniformivEXT` | `0x59A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1619 | `glReadnPixelsEXT` | `0x59A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1102 | `glDeleteSemaphoresEXT` | `0x59A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `glGenSemaphoresEXT` | `0x59A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `glIsSemaphoreEXT` | `0x59A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1663 | `glSignalSemaphoreEXT` | `0x59AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1805 | `glWaitSemaphoreEXT` | `0x59AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `glImportSemaphoreFdEXT` | `0x59AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 964 | `glActiveShaderProgramEXT` | `0x59AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 984 | `glBindProgramPipelineEXT` | `0x59AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1079 | `glCreateShaderProgramvEXT` | `0x59AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `glDeleteProgramPipelinesEXT` | `0x59B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `glGenProgramPipelinesEXT` | `0x59B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1315 | `glGetProgramPipelineInfoLogEXT` | `0x59B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `glGetProgramPipelineivEXT` | `0x59B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1442 | `glIsProgramPipelineEXT` | `0x59B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1541 | `glProgramParameteriEXT` | `0x59B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1543 | `glProgramUniform1fEXT` | `0x59B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1545 | `glProgramUniform1fvEXT` | `0x59B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1547 | `glProgramUniform1iEXT` | `0x59B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1549 | `glProgramUniform1ivEXT` | `0x59B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1551 | `glProgramUniform1uiEXT` | `0x59BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1553 | `glProgramUniform1uivEXT` | `0x59BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1555 | `glProgramUniform2fEXT` | `0x59BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1557 | `glProgramUniform2fvEXT` | `0x59BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1559 | `glProgramUniform2iEXT` | `0x59BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1561 | `glProgramUniform2ivEXT` | `0x59BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1563 | `glProgramUniform2uiEXT` | `0x59C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1565 | `glProgramUniform2uivEXT` | `0x59C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1567 | `glProgramUniform3fEXT` | `0x59C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1569 | `glProgramUniform3fvEXT` | `0x59C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1571 | `glProgramUniform3iEXT` | `0x59C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1573 | `glProgramUniform3ivEXT` | `0x59C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1575 | `glProgramUniform3uiEXT` | `0x59C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1577 | `glProgramUniform3uivEXT` | `0x59C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1579 | `glProgramUniform4fEXT` | `0x59C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `glProgramUniform4fvEXT` | `0x59C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1583 | `glProgramUniform4iEXT` | `0x59CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1585 | `glProgramUniform4ivEXT` | `0x59CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1587 | `glProgramUniform4uiEXT` | `0x59CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1589 | `glProgramUniform4uivEXT` | `0x59CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1591 | `glProgramUniformMatrix2fvEXT` | `0x59CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `glProgramUniformMatrix2x3fvEXT` | `0x59CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `glProgramUniformMatrix2x4fvEXT` | `0x59D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1597 | `glProgramUniformMatrix3fvEXT` | `0x59D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1599 | `glProgramUniformMatrix3x2fvEXT` | `0x59D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1601 | `glProgramUniformMatrix3x4fvEXT` | `0x59D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1603 | `glProgramUniformMatrix4fvEXT` | `0x59D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1605 | `glProgramUniformMatrix4x2fvEXT` | `0x59D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1607 | `glProgramUniformMatrix4x3fvEXT` | `0x59D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1778 | `glUseProgramStagesEXT` | `0x59D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1781 | `glValidateProgramPipelineEXT` | `0x59D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1514 | `glPatchParameteriEXT` | `0x59D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1342 | `glGetSamplerParameterIivEXT` | `0x59DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1346 | `glGetSamplerParameterIuivEXT` | `0x59DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1376 | `glGetTexParameterIivEXT` | `0x59DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1380 | `glGetTexParameterIuivEXT` | `0x59DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1638 | `glSamplerParameterIivEXT` | `0x59DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `glSamplerParameterIuivEXT` | `0x59DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1698 | `glTexParameterIivEXT` | `0x59E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1702 | `glTexParameterIuivEXT` | `0x59E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1673 | `glTexBufferEXT` | `0x59E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1676 | `glTexBufferRangeEXT` | `0x59E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1714 | `glTexStorage2DEXT` | `0x59E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1718 | `glTexStorage3DEXT` | `0x59E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1721 | `glTexStorageAttribs2DEXT` | `0x59E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1722 | `glTexStorageAttribs3DEXT` | `0x59E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `glDebugMessageControlKHR` | `0x59E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1087 | `glDebugMessageInsertKHR` | `0x59E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `glGetDebugMessageLogKHR` | `0x59EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1296 | `glGetObjectLabelKHR` | `0x59EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1298 | `glGetObjectPtrLabelKHR` | `0x59EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `glGetPointervKHR` | `0x59ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1508 | `glObjectLabelKHR` | `0x59EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `glObjectPtrLabelKHR` | `0x59EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1532 | `glPopDebugGroupKHR` | `0x59F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1610 | `glPushDebugGroupKHR` | `0x59F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1274 | `glGetGraphicsResetStatusKHR` | `0x59F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1413 | `glGetnUniformfvKHR` | `0x59F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1417 | `glGetnUniformivKHR` | `0x59F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1420 | `glGetnUniformuivKHR` | `0x59F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1620 | `glReadnPixelsKHR` | `0x59F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `glFramebufferParameteriMESA` | `0x59F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1266 | `glGetFramebufferParameterivMESA` | `0x59F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `glDeleteFencesNV` | `0x59F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `glFinishFenceNV` | `0x59FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `glGenFencesNV` | `0x59FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1255 | `glGetFenceivNV` | `0x59FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1436 | `glIsFenceNV` | `0x59FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1656 | `glSetFenceNV` | `0x59FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1671 | `glTestFenceNV` | `0x59FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `glBlitFramebufferNV` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1527 | `glPolygonModeNV` | `0x5A010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1159 | `glEGLImageTargetRenderbufferStorageOES` | `0x5A020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1161 | `glEGLImageTargetTexture2DOES` | `0x5A030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `glBlendEquationOES` | `0x5A040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1065 | `glCopyImageSubDataOES` | `0x5A050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `glBlendEquationSeparateiOES` | `0x5A060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `glBlendEquationiOES` | `0x5A070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `glBlendFuncSeparateiOES` | `0x5A080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | `glBlendFunciOES` | `0x5A090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1048 | `glColorMaskiOES` | `0x5A0A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1120 | `glDisableiOES` | `0x5A0B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `glEnableiOES` | `0x5A0C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1435 | `glIsEnablediOES` | `0x5A0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `glDrawElementsBaseVertexOES` | `0x5A0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `glDrawElementsInstancedBaseVertexOES` | `0x5A0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1150 | `glDrawRangeElementsBaseVertexOES` | `0x5A100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `glDrawTexfOES` | `0x5A110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1152 | `glDrawTexfvOES` | `0x5A120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1153 | `glDrawTexiOES` | `0x5A130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `glDrawTexivOES` | `0x5A140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1155 | `glDrawTexsOES` | `0x5A150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1156 | `glDrawTexsvOES` | `0x5A160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1157 | `glDrawTexxOES` | `0x5A170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1158 | `glDrawTexxvOES` | `0x5A180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `glBindFramebufferOES` | `0x5A190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `glBindRenderbufferOES` | `0x5A1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `glCheckFramebufferStatusOES` | `0x5A1B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1091 | `glDeleteFramebuffersOES` | `0x5A1C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1100 | `glDeleteRenderbuffersOES` | `0x5A1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `glFramebufferRenderbufferOES` | `0x5A1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1201 | `glFramebufferTexture2DOES` | `0x5A1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1214 | `glGenFramebuffersOES` | `0x5A200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `glGenRenderbuffersOES` | `0x5A210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `glGenerateMipmapOES` | `0x5A220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1263 | `glGetFramebufferAttachmentParameterivOES` | `0x5A230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1339 | `glGetRenderbufferParameterivOES` | `0x5A240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1438 | `glIsFramebufferOES` | `0x5A250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1446 | `glIsRenderbufferOES` | `0x5A260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1628 | `glRenderbufferStorageOES` | `0x5A270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1206 | `glFramebufferTextureOES` | `0x5A280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1310 | `glGetProgramBinaryOES` | `0x5A290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `glProgramBinaryOES` | `0x5A2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1247 | `glGetBufferPointervOES` | `0x5A2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1474 | `glMapBufferOES` | `0x5A2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1775 | `glUnmapBufferOES` | `0x5A2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1524 | `glPointSizePointerOES` | `0x5A2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1488 | `glMinSampleShadingOES` | `0x5A2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1515 | `glPatchParameteriOES` | `0x5A300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1055 | `glCompressedTexImage3DOES` | `0x5A310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1060 | `glCompressedTexSubImage3DOES` | `0x5A320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `glCopyTexSubImage3DOES` | `0x5A330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `glFramebufferTexture3DOES` | `0x5A340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1695 | `glTexImage3DOES` | `0x5A350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1734 | `glTexSubImage3DOES` | `0x5A360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1343 | `glGetSamplerParameterIivOES` | `0x5A370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1347 | `glGetSamplerParameterIuivOES` | `0x5A380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1377 | `glGetTexParameterIivOES` | `0x5A390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1381 | `glGetTexParameterIuivOES` | `0x5A3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1639 | `glSamplerParameterIivOES` | `0x5A3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1643 | `glSamplerParameterIuivOES` | `0x5A3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1699 | `glTexParameterIivOES` | `0x5A3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1703 | `glTexParameterIuivOES` | `0x5A3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1674 | `glTexBufferOES` | `0x5A3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1677 | `glTexBufferRangeOES` | `0x5A400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1720 | `glTexStorage3DMultisampleOES` | `0x5A410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `glBindVertexArrayOES` | `0x5A420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1108 | `glDeleteVertexArraysOES` | `0x5A430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `glGenVertexArraysOES` | `0x5A440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1454 | `glIsVertexArrayOES` | `0x5A450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `glFramebufferTextureMultiviewOVR` | `0x5A460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `glFramebufferFoveationConfigQCOM` | `0x5A470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1186 | `glFramebufferFoveationParametersQCOM` | `0x5A480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1662 | `glShadingRateQCOM` | `0x5A490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1736 | `glTextureFoveationParametersQCOM` | `0x5A4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1172 | `glEndTilingQCOM` | `0x5A4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1664 | `glStartTilingQCOM` | `0x5A4C0` | 5,245,257 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
