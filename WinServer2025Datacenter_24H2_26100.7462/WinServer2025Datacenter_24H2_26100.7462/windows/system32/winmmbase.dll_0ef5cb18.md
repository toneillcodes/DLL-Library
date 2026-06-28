# Binary Specification: winmmbase.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\winmmbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0ef5cb1886f2a1994ec74e09f317795b386291cfe3805e70d2cff9ff71e1b0fa`
* **Total Exported Functions:** 141

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 64 | `mixerGetLineControlsW` | `0x19D0` | 249 | UnwindData |  |
| 59 | `mixerGetControlDetailsW` | `0x1BC0` | 273 | UnwindData |  |
| 66 | `mixerGetLineInfoW` | `0x1CE0` | 628 | UnwindData |  |
| 69 | `mixerOpen` | `0x2200` | 1,518 | UnwindData |  |
| 109 | `waveInOpen` | `0x2AA0` | 182 | UnwindData |  |
| 107 | `waveInGetPosition` | `0x2FA0` | 27 | UnwindData |  |
| 128 | `waveOutOpen` | `0x3290` | 175 | UnwindData |  |
| 136 | `waveOutUnprepareHeader` | `0x3870` | 67 | UnwindData |  |
| 125 | `waveOutGetPosition` | `0x3C50` | 27 | UnwindData |  |
| 130 | `waveOutPrepareHeader` | `0x3FD0` | 60 | UnwindData |  |
| 137 | `waveOutWrite` | `0x43A0` | 69 | UnwindData |  |
| 26 | `midiInPrepareHeader` | `0x4760` | 72 | UnwindData |  |
| 99 | `waveInAddBuffer` | `0x5060` | 69 | UnwindData |  |
| 110 | `waveInPrepareHeader` | `0x5380` | 60 | UnwindData |  |
| 114 | `waveInUnprepareHeader` | `0x5880` | 67 | UnwindData |  |
| 122 | `waveOutGetNumDevs` | `0x5E70` | 128 | UnwindData |  |
| 47 | `midiOutShortMsg` | `0x5F00` | 335 | UnwindData |  |
| 108 | `waveInMessage` | `0x6060` | 127 | UnwindData |  |
| 127 | `waveOutMessage` | `0x7490` | 127 | UnwindData |  |
| 19 | `midiInGetDevCapsW` | `0x78E0` | 255 | UnwindData |  |
| 82 | `mmioFlush` | `0x79F0` | 152 | UnwindData |  |
| 131 | `waveOutReset` | `0x7BC0` | 87 | UnwindData |  |
| 24 | `midiInMessage` | `0x7DA0` | 127 | UnwindData |  |
| 126 | `waveOutGetVolume` | `0x7E30` | 187 | UnwindData |  |
| 116 | `waveOutClose` | `0x83E0` | 252 | UnwindData |  |
| 35 | `midiOutGetDevCapsW` | `0x86A0` | 249 | UnwindData |  |
| 39 | `midiOutGetNumDevs` | `0x90A0` | 85 | UnwindData |  |
| 118 | `waveOutGetDevCapsW` | `0x97F0` | 512 | UnwindData |  |
| 71 | `mmDrvInstall` | `0xA260` | 77 | UnwindData |  |
| 4 | `DrvGetModuleHandle` | `0xC090` | 145 | UnwindData |  |
| 5 | `GetDriverModuleHandle` | `0xC090` | 145 | UnwindData |  |
| 44 | `midiOutPrepareHeader` | `0xD030` | 630 | UnwindData |  |
| 3 | `DriverCallback` | `0xD320` | 262 | UnwindData |  |
| 75 | `mmTaskSignal` | `0xD430` | 56 | UnwindData |  |
| 16 | `midiInAddBuffer` | `0xD470` | 140 | UnwindData |  |
| 88 | `mmioRead` | `0xE4F0` | 739 | UnwindData |  |
| 7 | `SendDriverMessage` | `0xE950` | 320 | UnwindData |  |
| 78 | `mmioAscend` | `0xEAA0` | 301 | UnwindData |  |
| 80 | `mmioCreateChunk` | `0xEBE0` | 173 | UnwindData |  |
| 91 | `mmioSeek` | `0xECA0` | 294 | UnwindData |  |
| 97 | `mmioWrite` | `0xEDD0` | 470 | UnwindData |  |
| 6 | `OpenDriver` | `0xF030` | 135 | UnwindData |  |
| 106 | `waveInGetNumDevs` | `0xF7C0` | 85 | UnwindData |  |
| 42 | `midiOutMessage` | `0xF960` | 179 | UnwindData |  |
| 102 | `waveInGetDevCapsW` | `0xFC10` | 248 | UnwindData |  |
| 117 | `waveOutGetDevCapsA` | `0xFDE0` | 469 | UnwindData |  |
| 101 | `waveInGetDevCapsA` | `0x10170` | 446 | UnwindData |  |
| 83 | `mmioGetInfo` | `0x10390` | 113 | UnwindData |  |
| 1 | `CloseDriver` | `0x106B0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `mmioSetInfo` | `0x10A90` | 136 | UnwindData |  |
| 23 | `midiInGetNumDevs` | `0x10B20` | 85 | UnwindData |  |
| 48 | `midiOutUnprepareHeader` | `0x10B80` | 454 | UnwindData |  |
| 77 | `mmioAdvance` | `0x112C0` | 233 | UnwindData |  |
| 62 | `mixerGetID` | `0x113B0` | 58 | UnwindData |  |
| 79 | `mmioClose` | `0x133F0` | 113 | UnwindData |  |
| 84 | `mmioInstallIOProcA` | `0x13470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `mmioInstallIOProcW` | `0x13490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `mmioOpenA` | `0x134B0` | 581 | UnwindData |  |
| 87 | `mmioOpenW` | `0x13700` | 522 | UnwindData |  |
| 89 | `mmioRenameA` | `0x13910` | 364 | UnwindData |  |
| 90 | `mmioRenameW` | `0x13A90` | 373 | UnwindData |  |
| 92 | `mmioSendMessage` | `0x13C10` | 91 | UnwindData |  |
| 93 | `mmioSetBuffer` | `0x13C80` | 550 | UnwindData |  |
| 95 | `mmioStringToFOURCCA` | `0x13EB0` | 121 | UnwindData |  |
| 96 | `mmioStringToFOURCCW` | `0x13F30` | 169 | UnwindData |  |
| 81 | `mmioDescend` | `0x13FE0` | 531 | UnwindData |  |
| 2 | `DefDriverProc` | `0x14730` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `auxGetDevCapsA` | `0x14860` | 363 | UnwindData |  |
| 9 | `auxGetDevCapsW` | `0x149E0` | 153 | UnwindData |  |
| 10 | `auxGetNumDevs` | `0x14A80` | 64 | UnwindData |  |
| 11 | `auxGetVolume` | `0x14AD0` | 96 | UnwindData |  |
| 12 | `auxOutMessage` | `0x14B40` | 210 | UnwindData |  |
| 13 | `auxSetVolume` | `0x14C20` | 85 | UnwindData |  |
| 14 | `midiConnect` | `0x14F50` | 104 | UnwindData |  |
| 15 | `midiDisconnect` | `0x14FC0` | 101 | UnwindData |  |
| 49 | `midiStreamClose` | `0x15320` | 443 | UnwindData |  |
| 50 | `midiStreamOpen` | `0x15580` | 1,585 | UnwindData |  |
| 51 | `midiStreamOut` | `0x15BC0` | 735 | UnwindData |  |
| 52 | `midiStreamPause` | `0x15EB0` | 58 | UnwindData |  |
| 53 | `midiStreamPosition` | `0x15EF0` | 92 | UnwindData |  |
| 54 | `midiStreamProperty` | `0x15F60` | 101 | UnwindData |  |
| 55 | `midiStreamRestart` | `0x15FD0` | 390 | UnwindData |  |
| 56 | `midiStreamStop` | `0x16160` | 58 | UnwindData |  |
| 76 | `mmTaskYield` | `0x18920` | 7,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `midiInClose` | `0x1A600` | 245 | UnwindData |  |
| 18 | `midiInGetDevCapsA` | `0x1A7E0` | 459 | UnwindData |  |
| 20 | `midiInGetErrorTextA` | `0x1A9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `midiOutGetErrorTextA` | `0x1A9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `midiInGetErrorTextW` | `0x1A9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `midiOutGetErrorTextW` | `0x1A9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `midiInGetID` | `0x1AA00` | 66 | UnwindData |  |
| 25 | `midiInOpen` | `0x1AA50` | 455 | UnwindData |  |
| 27 | `midiInReset` | `0x1AC20` | 84 | UnwindData |  |
| 28 | `midiInStart` | `0x1AC80` | 66 | UnwindData |  |
| 29 | `midiInStop` | `0x1ACD0` | 66 | UnwindData |  |
| 30 | `midiInUnprepareHeader` | `0x1AD20` | 177 | UnwindData |  |
| 31 | `midiOutCacheDrumPatches` | `0x1ADE0` | 200 | UnwindData |  |
| 32 | `midiOutCachePatches` | `0x1AEB0` | 200 | UnwindData |  |
| 33 | `midiOutClose` | `0x1AF80` | 245 | UnwindData |  |
| 34 | `midiOutGetDevCapsA` | `0x1B160` | 493 | UnwindData |  |
| 38 | `midiOutGetID` | `0x1B360` | 66 | UnwindData |  |
| 40 | `midiOutGetVolume` | `0x1B3B0` | 271 | UnwindData |  |
| 41 | `midiOutLongMsg` | `0x1B4D0` | 205 | UnwindData |  |
| 43 | `midiOutOpen` | `0x1B5B0` | 539 | UnwindData |  |
| 45 | `midiOutReset` | `0x1B7E0` | 133 | UnwindData |  |
| 46 | `midiOutSetVolume` | `0x1B870` | 212 | UnwindData |  |
| 57 | `mixerClose` | `0x1C630` | 435 | UnwindData |  |
| 58 | `mixerGetControlDetailsA` | `0x1C7F0` | 342 | UnwindData |  |
| 60 | `mixerGetDevCapsA` | `0x1C950` | 261 | UnwindData |  |
| 61 | `mixerGetDevCapsW` | `0x1CA60` | 299 | UnwindData |  |
| 63 | `mixerGetLineControlsA` | `0x1CBA0` | 443 | UnwindData |  |
| 65 | `mixerGetLineInfoA` | `0x1CD70` | 335 | UnwindData |  |
| 67 | `mixerGetNumDevs` | `0x1CED0` | 64 | UnwindData |  |
| 68 | `mixerMessage` | `0x1CF20` | 123 | UnwindData |  |
| 70 | `mixerSetControlDetails` | `0x1CFB0` | 287 | UnwindData |  |
| 98 | `sndOpenSound` | `0x1D580` | 323 | UnwindData |  |
| 138 | `winmmbaseFreeMMEHandles` | `0x1D6D0` | 508 | UnwindData |  |
| 139 | `winmmbaseGetWOWHandle` | `0x1D8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `winmmbaseHandle32FromHandle16` | `0x1D8F0` | 157 | UnwindData |  |
| 141 | `winmmbaseSetWOWHandle` | `0x1D9A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `mmGetCurrentTask` | `0x1DA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `mmTaskBlock` | `0x1DA40` | 99 | UnwindData |  |
| 74 | `mmTaskCreate` | `0x1DAB0` | 313 | UnwindData |  |
| 100 | `waveInClose` | `0x1DF10` | 245 | UnwindData |  |
| 103 | `waveInGetErrorTextA` | `0x1E010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `waveOutGetErrorTextA` | `0x1E010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `waveInGetErrorTextW` | `0x1E030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `waveOutGetErrorTextW` | `0x1E030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `waveInGetID` | `0x1E050` | 66 | UnwindData |  |
| 111 | `waveInReset` | `0x1E0A0` | 84 | UnwindData |  |
| 112 | `waveInStart` | `0x1E100` | 66 | UnwindData |  |
| 113 | `waveInStop` | `0x1E150` | 66 | UnwindData |  |
| 115 | `waveOutBreakLoop` | `0x1E1A0` | 66 | UnwindData |  |
| 121 | `waveOutGetID` | `0x1E1F0` | 66 | UnwindData |  |
| 123 | `waveOutGetPitch` | `0x1E240` | 85 | UnwindData |  |
| 124 | `waveOutGetPlaybackRate` | `0x1E2A0` | 85 | UnwindData |  |
| 129 | `waveOutPause` | `0x1E300` | 66 | UnwindData |  |
| 132 | `waveOutRestart` | `0x1E350` | 66 | UnwindData |  |
| 133 | `waveOutSetPitch` | `0x1E3A0` | 74 | UnwindData |  |
| 134 | `waveOutSetPlaybackRate` | `0x1E3F0` | 74 | UnwindData |  |
| 135 | `waveOutSetVolume` | `0x1E440` | 173 | UnwindData |  |
