# Binary Specification: winmm.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\winmm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `95f9d6069156740b12c125fb6f84e65de9a235b70c61369229f388c7cae8621c`
* **Total Exported Functions:** 181

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 143 | `timeSetEvent` | `0x2420` | 36 | UnwindData |  |
| 142 | `timeKillEvent` | `0x2940` | 85 | UnwindData |  |
| 141 | `timeGetTime` | `0x4220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `timeEndPeriod` | `0x4240` | 10,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `timeBeginPeriod` | `0x6990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `PlaySoundW` | `0x69B0` | 115 | UnwindData |  |
| 26 | `joyGetPosEx` | `0x7400` | 1,422 | UnwindData |  |
| 182 | `waveOutWrite` | `0x94E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `waveInAddBuffer` | `0x9550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `waveOutPrepareHeader` | `0x9570` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `waveInGetPosition` | `0x9770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `waveOutGetPosition` | `0x9790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `waveOutUnprepareHeader` | `0x97B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `timeGetDevCaps` | `0x97D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `midiInAddBuffer` | `0x9800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `waveInUnprepareHeader` | `0x9820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `midiInPrepareHeader` | `0x9840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `timeGetSystemTime` | `0x9860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `waveInPrepareHeader` | `0x9880` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `mciDriverYield` | `0x9A00` | 174 | UnwindData |  |
| 45 | `mciSendCommandW` | `0x9DB0` | 302 | UnwindData |  |
| 172 | `waveOutMessage` | `0xA170` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `waveInGetNumDevs` | `0xA1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `waveOutGetNumDevs` | `0xA200` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `waveInMessage` | `0xA650` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `midiOutShortMsg` | `0xA6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `waveInGetDevCapsW` | `0xA710` | 5,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `midiInGetNumDevs` | `0xBC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `mmioRead` | `0xBC20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `mixerOpen` | `0xBC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `midiOutLongMsg` | `0xBC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `midiOutPrepareHeader` | `0xBCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `mixerGetDevCapsW` | `0xBCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `waveOutOpen` | `0xBCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `mixerGetID` | `0xBD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `waveOutGetDevCapsA` | `0xBD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `waveInOpen` | `0xBD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `midiOutUnprepareHeader` | `0xBD60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `mixerGetControlDetailsW` | `0xBD80` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `midiInGetDevCapsW` | `0xC0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `mmioWrite` | `0xC100` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `midiOutMessage` | `0xC140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `waveOutGetVolume` | `0xC160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `midiInMessage` | `0xC180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `mmioCreateChunk` | `0xC1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `midiOutGetDevCapsW` | `0xC1C0` | 12,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `joyConfigChanged` | `0xF180` | 95 | UnwindData |  |
| 22 | `joyGetDevCapsA` | `0xF1F0` | 759 | UnwindData |  |
| 23 | `joyGetDevCapsW` | `0xF4F0` | 263 | UnwindData |  |
| 24 | `joyGetNumDevs` | `0xF600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `joyGetPos` | `0xF610` | 107 | UnwindData |  |
| 27 | `joyGetThreshold` | `0xF690` | 198 | UnwindData |  |
| 28 | `joyReleaseCapture` | `0xFAA0` | 173 | UnwindData |  |
| 29 | `joySetCapture` | `0xFB60` | 623 | UnwindData |  |
| 30 | `joySetThreshold` | `0xFDE0` | 206 | UnwindData |  |
| 4 | `CloseDriver` | `0xFF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DefDriverProc` | `0xFF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DriverCallback` | `0xFFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DrvGetModuleHandle` | `0xFFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetDriverModuleHandle` | `0xFFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `PlaySound` | `0xFFF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | *Ordinal Only* | `0xFFF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `OpenDriver` | `0x10000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `SendDriverMessage` | `0x10020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `auxGetDevCapsA` | `0x10040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `auxGetDevCapsW` | `0x10060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `auxGetNumDevs` | `0x10080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `auxGetVolume` | `0x100A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `auxOutMessage` | `0x100C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `auxSetVolume` | `0x100E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `midiConnect` | `0x10100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `midiDisconnect` | `0x10120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `midiInClose` | `0x10140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `midiInGetDevCapsA` | `0x10160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `midiInGetErrorTextA` | `0x10180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `midiInGetErrorTextW` | `0x101A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `midiInGetID` | `0x101C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `midiInOpen` | `0x101E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `midiInReset` | `0x10200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `midiInStart` | `0x10220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `midiInStop` | `0x10240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `midiInUnprepareHeader` | `0x10260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `midiOutCacheDrumPatches` | `0x10280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `midiOutCachePatches` | `0x102A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `midiOutClose` | `0x102C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `midiOutGetDevCapsA` | `0x102E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `midiOutGetErrorTextA` | `0x10300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `midiOutGetErrorTextW` | `0x10320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `midiOutGetID` | `0x10340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `midiOutGetNumDevs` | `0x10360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `midiOutGetVolume` | `0x10380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `midiOutOpen` | `0x103A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `midiOutReset` | `0x103C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `midiOutSetVolume` | `0x103E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `midiStreamClose` | `0x10400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `midiStreamOpen` | `0x10420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `midiStreamOut` | `0x10440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `midiStreamPause` | `0x10460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `midiStreamPosition` | `0x10480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `midiStreamProperty` | `0x104A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `midiStreamRestart` | `0x104C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `midiStreamStop` | `0x104E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `mixerClose` | `0x10500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `mixerGetControlDetailsA` | `0x10520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `mixerGetDevCapsA` | `0x10540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `mixerGetLineControlsA` | `0x10560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `mixerGetLineControlsW` | `0x10580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `mixerGetLineInfoA` | `0x105A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `mixerGetLineInfoW` | `0x105C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `mixerGetNumDevs` | `0x105E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `mixerMessage` | `0x10600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `mixerSetControlDetails` | `0x10620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `mmDrvInstall` | `0x10640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `mmGetCurrentTask` | `0x10660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `mmTaskBlock` | `0x10680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `mmTaskCreate` | `0x106A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `mmTaskSignal` | `0x106C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `mmTaskYield` | `0x106E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `mmioAdvance` | `0x10700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `mmioAscend` | `0x10720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `mmioClose` | `0x10740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `mmioDescend` | `0x10760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `mmioFlush` | `0x10780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `mmioGetInfo` | `0x107A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `mmioInstallIOProcA` | `0x107C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `mmioInstallIOProcW` | `0x107E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `mmioOpenA` | `0x10800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `mmioOpenW` | `0x10820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `mmioRenameA` | `0x10840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `mmioRenameW` | `0x10860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `mmioSeek` | `0x10880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `mmioSendMessage` | `0x108A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `mmioSetBuffer` | `0x108C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `mmioSetInfo` | `0x108E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `mmioStringToFOURCCA` | `0x10900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `mmioStringToFOURCCW` | `0x10920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `waveInClose` | `0x10940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `waveInGetDevCapsA` | `0x10960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `waveInGetErrorTextA` | `0x10980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `waveInGetErrorTextW` | `0x109A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `waveInGetID` | `0x109C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `waveInReset` | `0x109E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `waveInStart` | `0x10A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `waveInStop` | `0x10A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `waveOutBreakLoop` | `0x10A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `waveOutClose` | `0x10A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `waveOutGetDevCapsW` | `0x10A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `waveOutGetErrorTextA` | `0x10AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `waveOutGetErrorTextW` | `0x10AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `waveOutGetID` | `0x10AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `waveOutGetPitch` | `0x10B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `waveOutGetPlaybackRate` | `0x10B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `waveOutPause` | `0x10B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `waveOutReset` | `0x10B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `waveOutRestart` | `0x10B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `waveOutSetPitch` | `0x10BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `waveOutSetPlaybackRate` | `0x10BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `waveOutSetVolume` | `0x10BE0` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `mciExecute` | `0x113B0` | 463 | UnwindData |  |
| 40 | `mciGetErrorStringA` | `0x12680` | 282 | UnwindData |  |
| 41 | `mciGetErrorStringW` | `0x127A0` | 283 | UnwindData |  |
| 44 | `mciSendCommandA` | `0x12AD0` | 2,195 | UnwindData |  |
| 46 | `mciSendStringA` | `0x13370` | 513 | UnwindData |  |
| 47 | `mciSendStringW` | `0x13580` | 109 | UnwindData |  |
| 33 | `mciFreeCommandResource` | `0x14360` | 410 | UnwindData |  |
| 43 | `mciLoadCommandResource` | `0x14560` | 1,071 | UnwindData |  |
| 31 | `mciDriverNotify` | `0x164E0` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `mciGetCreatorTask` | `0x168F0` | 110 | UnwindData |  |
| 35 | `mciGetDeviceIDA` | `0x16970` | 85 | UnwindData |  |
| 36 | `mciGetDeviceIDFromElementIDA` | `0x169D0` | 78 | UnwindData |  |
| 37 | `mciGetDeviceIDFromElementIDW` | `0x16A30` | 257 | UnwindData |  |
| 38 | `mciGetDeviceIDW` | `0x16B40` | 36 | UnwindData |  |
| 39 | `mciGetDriverData` | `0x16B70` | 167 | UnwindData |  |
| 42 | `mciGetYieldProc` | `0x16C20` | 147 | UnwindData |  |
| 48 | `mciSetDriverData` | `0x171A0` | 172 | UnwindData |  |
| 49 | `mciSetYieldProc` | `0x17260` | 132 | UnwindData |  |
| 11 | `PlaySoundA` | `0x1B7E0` | 239 | UnwindData |  |
| 135 | `sndPlaySoundA` | `0x1BC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `sndPlaySoundW` | `0x1BC10` | 2,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `WOWAppExit` | `0x1C730` | 401 | UnwindData |  |
| 134 | `mmsystemGetVersion` | `0x1C8D0` | 0 | Indeterminate |  |
