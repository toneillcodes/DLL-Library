# Binary Specification: winmmbase.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\winmmbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a35aa29a79f3a2ce238e3db8a201fac4825a04dd42c00e7f33c90b0dd2d8ebea`
* **Total Exported Functions:** 141

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 64 | `mixerGetLineControlsW` | `0x1990` | 249 | UnwindData |  |
| 59 | `mixerGetControlDetailsW` | `0x1B80` | 273 | UnwindData |  |
| 66 | `mixerGetLineInfoW` | `0x1CA0` | 628 | UnwindData |  |
| 69 | `mixerOpen` | `0x21C0` | 1,518 | UnwindData |  |
| 71 | `mmDrvInstall` | `0x27C0` | 1,048 | UnwindData |  |
| 109 | `waveInOpen` | `0x2E90` | 182 | UnwindData |  |
| 107 | `waveInGetPosition` | `0x3390` | 27 | UnwindData |  |
| 128 | `waveOutOpen` | `0x3680` | 175 | UnwindData |  |
| 136 | `waveOutUnprepareHeader` | `0x3C60` | 67 | UnwindData |  |
| 125 | `waveOutGetPosition` | `0x4040` | 27 | UnwindData |  |
| 130 | `waveOutPrepareHeader` | `0x43C0` | 60 | UnwindData |  |
| 137 | `waveOutWrite` | `0x4790` | 69 | UnwindData |  |
| 26 | `midiInPrepareHeader` | `0x4B50` | 72 | UnwindData |  |
| 99 | `waveInAddBuffer` | `0x5450` | 69 | UnwindData |  |
| 110 | `waveInPrepareHeader` | `0x5770` | 60 | UnwindData |  |
| 114 | `waveInUnprepareHeader` | `0x5C70` | 67 | UnwindData |  |
| 122 | `waveOutGetNumDevs` | `0x6260` | 128 | UnwindData |  |
| 47 | `midiOutShortMsg` | `0x62F0` | 335 | UnwindData |  |
| 108 | `waveInMessage` | `0x6450` | 127 | UnwindData |  |
| 127 | `waveOutMessage` | `0x7430` | 127 | UnwindData |  |
| 19 | `midiInGetDevCapsW` | `0x7880` | 255 | UnwindData |  |
| 82 | `mmioFlush` | `0x7990` | 152 | UnwindData |  |
| 131 | `waveOutReset` | `0x7B60` | 87 | UnwindData |  |
| 24 | `midiInMessage` | `0x7D40` | 127 | UnwindData |  |
| 126 | `waveOutGetVolume` | `0x7DD0` | 187 | UnwindData |  |
| 97 | `mmioWrite` | `0x82E0` | 470 | UnwindData |  |
| 116 | `waveOutClose` | `0x8550` | 252 | UnwindData |  |
| 35 | `midiOutGetDevCapsW` | `0x8820` | 249 | UnwindData |  |
| 118 | `waveOutGetDevCapsW` | `0x9900` | 512 | UnwindData |  |
| 80 | `mmioCreateChunk` | `0x9E60` | 173 | UnwindData |  |
| 91 | `mmioSeek` | `0x9F20` | 294 | UnwindData |  |
| 78 | `mmioAscend` | `0xA050` | 301 | UnwindData |  |
| 4 | `DrvGetModuleHandle` | `0xC1B0` | 145 | UnwindData |  |
| 5 | `GetDriverModuleHandle` | `0xC1B0` | 145 | UnwindData |  |
| 44 | `midiOutPrepareHeader` | `0xD040` | 630 | UnwindData |  |
| 3 | `DriverCallback` | `0xD330` | 262 | UnwindData |  |
| 75 | `mmTaskSignal` | `0xD440` | 56 | UnwindData |  |
| 16 | `midiInAddBuffer` | `0xD480` | 140 | UnwindData |  |
| 88 | `mmioRead` | `0xE500` | 739 | UnwindData |  |
| 7 | `SendDriverMessage` | `0xEE90` | 320 | UnwindData |  |
| 6 | `OpenDriver` | `0xEFE0` | 135 | UnwindData |  |
| 106 | `waveInGetNumDevs` | `0xF770` | 85 | UnwindData |  |
| 42 | `midiOutMessage` | `0xF910` | 179 | UnwindData |  |
| 102 | `waveInGetDevCapsW` | `0xFBC0` | 248 | UnwindData |  |
| 117 | `waveOutGetDevCapsA` | `0xFD90` | 469 | UnwindData |  |
| 101 | `waveInGetDevCapsA` | `0x10070` | 446 | UnwindData |  |
| 83 | `mmioGetInfo` | `0x10290` | 113 | UnwindData |  |
| 1 | `CloseDriver` | `0x105B0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `mmioSetInfo` | `0x10990` | 136 | UnwindData |  |
| 23 | `midiInGetNumDevs` | `0x10A20` | 69 | UnwindData |  |
| 39 | `midiOutGetNumDevs` | `0x10A70` | 69 | UnwindData |  |
| 48 | `midiOutUnprepareHeader` | `0x10AC0` | 454 | UnwindData |  |
| 77 | `mmioAdvance` | `0x11210` | 233 | UnwindData |  |
| 62 | `mixerGetID` | `0x11300` | 58 | UnwindData |  |
| 79 | `mmioClose` | `0x13340` | 113 | UnwindData |  |
| 84 | `mmioInstallIOProcA` | `0x133C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `mmioInstallIOProcW` | `0x133E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `mmioOpenA` | `0x13400` | 581 | UnwindData |  |
| 87 | `mmioOpenW` | `0x13650` | 522 | UnwindData |  |
| 89 | `mmioRenameA` | `0x13860` | 364 | UnwindData |  |
| 90 | `mmioRenameW` | `0x139E0` | 373 | UnwindData |  |
| 92 | `mmioSendMessage` | `0x13B60` | 91 | UnwindData |  |
| 93 | `mmioSetBuffer` | `0x13BD0` | 550 | UnwindData |  |
| 95 | `mmioStringToFOURCCA` | `0x13E00` | 121 | UnwindData |  |
| 96 | `mmioStringToFOURCCW` | `0x13E80` | 169 | UnwindData |  |
| 81 | `mmioDescend` | `0x13F30` | 531 | UnwindData |  |
| 2 | `DefDriverProc` | `0x145A0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `auxGetDevCapsA` | `0x146D0` | 363 | UnwindData |  |
| 9 | `auxGetDevCapsW` | `0x14850` | 153 | UnwindData |  |
| 10 | `auxGetNumDevs` | `0x148F0` | 64 | UnwindData |  |
| 11 | `auxGetVolume` | `0x14940` | 96 | UnwindData |  |
| 12 | `auxOutMessage` | `0x149B0` | 210 | UnwindData |  |
| 13 | `auxSetVolume` | `0x14A90` | 85 | UnwindData |  |
| 14 | `midiConnect` | `0x14DC0` | 104 | UnwindData |  |
| 15 | `midiDisconnect` | `0x14E30` | 101 | UnwindData |  |
| 49 | `midiStreamClose` | `0x15190` | 443 | UnwindData |  |
| 50 | `midiStreamOpen` | `0x153F0` | 1,585 | UnwindData |  |
| 51 | `midiStreamOut` | `0x15A30` | 735 | UnwindData |  |
| 52 | `midiStreamPause` | `0x15D20` | 58 | UnwindData |  |
| 53 | `midiStreamPosition` | `0x15D60` | 92 | UnwindData |  |
| 54 | `midiStreamProperty` | `0x15DD0` | 101 | UnwindData |  |
| 55 | `midiStreamRestart` | `0x15E40` | 390 | UnwindData |  |
| 56 | `midiStreamStop` | `0x15FD0` | 58 | UnwindData |  |
| 17 | `midiInClose` | `0x160C0` | 245 | UnwindData |  |
| 18 | `midiInGetDevCapsA` | `0x162A0` | 459 | UnwindData |  |
| 20 | `midiInGetErrorTextA` | `0x16480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `midiOutGetErrorTextA` | `0x16480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `midiInGetErrorTextW` | `0x164A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `midiOutGetErrorTextW` | `0x164A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `midiInGetID` | `0x164C0` | 66 | UnwindData |  |
| 25 | `midiInOpen` | `0x16510` | 455 | UnwindData |  |
| 27 | `midiInReset` | `0x166E0` | 84 | UnwindData |  |
| 28 | `midiInStart` | `0x16740` | 66 | UnwindData |  |
| 29 | `midiInStop` | `0x16790` | 66 | UnwindData |  |
| 30 | `midiInUnprepareHeader` | `0x167E0` | 177 | UnwindData |  |
| 31 | `midiOutCacheDrumPatches` | `0x168A0` | 200 | UnwindData |  |
| 32 | `midiOutCachePatches` | `0x16970` | 200 | UnwindData |  |
| 33 | `midiOutClose` | `0x16A40` | 245 | UnwindData |  |
| 34 | `midiOutGetDevCapsA` | `0x16C20` | 493 | UnwindData |  |
| 38 | `midiOutGetID` | `0x16E20` | 66 | UnwindData |  |
| 40 | `midiOutGetVolume` | `0x16E70` | 271 | UnwindData |  |
| 41 | `midiOutLongMsg` | `0x16F90` | 205 | UnwindData |  |
| 43 | `midiOutOpen` | `0x17070` | 539 | UnwindData |  |
| 45 | `midiOutReset` | `0x172A0` | 133 | UnwindData |  |
| 46 | `midiOutSetVolume` | `0x17330` | 212 | UnwindData |  |
| 57 | `mixerClose` | `0x17BC0` | 435 | UnwindData |  |
| 58 | `mixerGetControlDetailsA` | `0x17D80` | 342 | UnwindData |  |
| 60 | `mixerGetDevCapsA` | `0x17EE0` | 261 | UnwindData |  |
| 61 | `mixerGetDevCapsW` | `0x17FF0` | 299 | UnwindData |  |
| 63 | `mixerGetLineControlsA` | `0x18130` | 443 | UnwindData |  |
| 65 | `mixerGetLineInfoA` | `0x18300` | 335 | UnwindData |  |
| 67 | `mixerGetNumDevs` | `0x18460` | 64 | UnwindData |  |
| 68 | `mixerMessage` | `0x184B0` | 123 | UnwindData |  |
| 70 | `mixerSetControlDetails` | `0x18540` | 287 | UnwindData |  |
| 98 | `sndOpenSound` | `0x1A280` | 323 | UnwindData |  |
| 138 | `winmmbaseFreeMMEHandles` | `0x1A3D0` | 508 | UnwindData |  |
| 139 | `winmmbaseGetWOWHandle` | `0x1A5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `winmmbaseHandle32FromHandle16` | `0x1A5F0` | 157 | UnwindData |  |
| 141 | `winmmbaseSetWOWHandle` | `0x1A6A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `mmGetCurrentTask` | `0x1A720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `mmTaskBlock` | `0x1A740` | 99 | UnwindData |  |
| 74 | `mmTaskCreate` | `0x1A7B0` | 313 | UnwindData |  |
| 76 | `mmTaskYield` | `0x1A8F0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `waveInClose` | `0x1AC20` | 245 | UnwindData |  |
| 103 | `waveInGetErrorTextA` | `0x1AD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `waveOutGetErrorTextA` | `0x1AD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `waveInGetErrorTextW` | `0x1AD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `waveOutGetErrorTextW` | `0x1AD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `waveInGetID` | `0x1AD60` | 66 | UnwindData |  |
| 111 | `waveInReset` | `0x1ADB0` | 84 | UnwindData |  |
| 112 | `waveInStart` | `0x1AE10` | 66 | UnwindData |  |
| 113 | `waveInStop` | `0x1AE60` | 66 | UnwindData |  |
| 115 | `waveOutBreakLoop` | `0x1AEB0` | 66 | UnwindData |  |
| 121 | `waveOutGetID` | `0x1AF00` | 66 | UnwindData |  |
| 123 | `waveOutGetPitch` | `0x1AF50` | 85 | UnwindData |  |
| 124 | `waveOutGetPlaybackRate` | `0x1AFB0` | 85 | UnwindData |  |
| 129 | `waveOutPause` | `0x1B010` | 66 | UnwindData |  |
| 132 | `waveOutRestart` | `0x1B060` | 66 | UnwindData |  |
| 133 | `waveOutSetPitch` | `0x1B0B0` | 74 | UnwindData |  |
| 134 | `waveOutSetPlaybackRate` | `0x1B100` | 74 | UnwindData |  |
| 135 | `waveOutSetVolume` | `0x1B150` | 173 | UnwindData |  |
