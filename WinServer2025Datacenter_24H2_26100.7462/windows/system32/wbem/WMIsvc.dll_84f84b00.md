# Binary Specification: WMIsvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\WMIsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `84f84b008d5224e75b546782cf5dcdad1c6d3f89eb49fba26c81d51775941b7c`
* **Total Exported Functions:** 334

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `??0CInCritSec@@QEAA@PEAU_RTL_CRITICAL_SECTION@@@Z` | `0x4B80` | 48 | UnwindData |  |
| 260 | `?InternalAddRef@CUnkInternal@@QEAAKXZ` | `0x90D0` | 7,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `IsImproperShutdownDetected` | `0xACF0` | 1,259 | UnwindData |  |
| 67 | `??1CInCritSec@@QEAA@XZ` | `0xB6A0` | 26 | UnwindData |  |
| 271 | `IsShutDown` | `0xB980` | 1,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `?GetStatus@C9XAce@@UEAAKXZ` | `0xBF80` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `ServiceMain` | `0xC9E0` | 343 | UnwindData |  |
| 13 | `??0CCritSec@@QEAA@XZ` | `0xD1F0` | 49 | UnwindData |  |
| 30 | `??0CTraceSessionControl@@QEAA@XZ` | `0xD5F0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `?ObjectDestroyed@CContainerControl@@UEAAXPEAUIUnknown@@@Z` | `0xD6E0` | 7,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0CArena@@QEAA@$$QEAV0@@Z` | `0xF380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0CArena@@QEAA@AEBV0@@Z` | `0xF380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0CArena@@QEAA@XZ` | `0xF380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `??0CWin32DefaultArena@@QEAA@AEBV0@@Z` | `0xF3A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `??0CWin32DefaultArena@@QEAA@XZ` | `0xF3A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `??1CWin32DefaultArena@@QEAA@XZ` | `0xF3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `??4CArena@@QEAAAEAV0@$$QEAV0@@Z` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??4CArena@@QEAAAEAV0@AEBV0@@Z` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `??4CBaseAce@@QEAAAEAV0@AEBV0@@Z` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `??4CLifeControl@@QEAAAEAV0@$$QEAV0@@Z` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `??4CLifeControl@@QEAAAEAV0@AEBV0@@Z` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `??4CNtSecurity@@QEAAAEAV0@$$QEAV0@@Z` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `??4CNtSecurity@@QEAAAEAV0@AEBV0@@Z` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `??4CPersistentConfig@@QEAAAEAV0@$$QEAV0@@Z` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `??4CPersistentConfig@@QEAAAEAV0@AEBV0@@Z` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `??4CWin32DefaultArena@@QEAAAEAV0@AEBV0@@Z` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `??4MD5@@QEAAAEAV0@$$QEAV0@@Z` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `??4MD5@@QEAAAEAV0@AEBV0@@Z` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?GetInnerUnknown@CUnk@@QEAAPEAUIUnknown@@XZ` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `?GetStringPointerByRef@WString@@QEBAAEBQEBGXZ` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `?GetUnknown@CUnkInternal@@QEAAPEAUIUnknown@@XZ` | `0xF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `?Alloc@CWin32DefaultArena@@UEAAPEAX_K@Z` | `0xF3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `?Free@CWin32DefaultArena@@UEAAHPEAX@Z` | `0xF410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `?Realloc@CWin32DefaultArena@@UEAAPEAXPEAX_K@Z` | `0xF430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `?WbemSysFreeString@CWin32DefaultArena@@SAXPEAG@Z` | `0xF450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0C9XAce@@QEAA@AEBV0@@Z` | `0xF470` | 56 | UnwindData |  |
| 2 | `??0C9XAce@@QEAA@XZ` | `0xF4B0` | 35 | UnwindData |  |
| 6 | `??0CBaseAce@@QEAA@AEBV0@@Z` | `0xF4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0CBaseAce@@QEAA@XZ` | `0xF4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0CCheckedInCritSec@@QEAA@PEAVCCritSec@@@Z` | `0xF500` | 41 | UnwindData |  |
| 9 | `??0CCircularQueue@@QEAA@XZ` | `0xF530` | 39 | UnwindData |  |
| 10 | `??0CContainerControl@@QEAA@$$QEAV0@@Z` | `0xF560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0CContainerControl@@QEAA@AEBV0@@Z` | `0xF560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0CContainerControl@@QEAA@PEAUIUnknown@@@Z` | `0xF580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??0CEnterWbemCriticalSection@@QEAA@PEAVCWbemCriticalSection@@K@Z` | `0xF5A0` | 55 | UnwindData |  |
| 15 | `??0CEventLog@@QEAA@AEBV0@@Z` | `0xF5E0` | 123 | UnwindData |  |
| 16 | `??0CEventLogRecord@@QEAA@AEAV0@@Z` | `0xF670` | 79 | UnwindData |  |
| 17 | `??0CHaltable@@QEAA@AEBV0@@Z` | `0xF6D0` | 66 | UnwindData |  |
| 18 | `??0CHex@@QEAA@J@Z` | `0xF720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??0CWbemInterval@@IEAA@K@Z` | `0xF720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0CInsertionString@@QEAA@$$QEAV0@@Z` | `0xF730` | 52 | UnwindData |  |
| 21 | `??0CInsertionString@@QEAA@AEBV0@@Z` | `0xF730` | 52 | UnwindData |  |
| 22 | `??0CInsertionString@@QEAA@PEBD@Z` | `0xF770` | 43 | UnwindData |  |
| 23 | `??0CInsertionString@@QEAA@PEBG@Z` | `0xF7B0` | 43 | UnwindData |  |
| 24 | `??0CInsertionString@@QEAA@XZ` | `0xF7F0` | 46 | UnwindData |  |
| 25 | `??0CLifeControl@@QEAA@$$QEAV0@@Z` | `0xF830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??0CLifeControl@@QEAA@AEBV0@@Z` | `0xF830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??0CLifeControl@@QEAA@XZ` | `0xF830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??0CNtAce@@QEAA@XZ` | `0xF850` | 42 | UnwindData |  |
| 29 | `??0CNtSid@@QEAA@XZ` | `0xF880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??0CUnk@@QEAA@AEBV0@@Z` | `0xF8A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??0CUnkInternal@@QEAA@AEBV0@@Z` | `0xF8D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??0CUnkInternal@@QEAA@PEAVCLifeControl@@@Z` | `0xF900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??0CVar@@QEAA@D@Z` | `0xF920` | 51 | UnwindData |  |
| 35 | `??0CVar@@QEAA@E@Z` | `0xF960` | 51 | UnwindData |  |
| 36 | `??0CVar@@QEAA@F@Z` | `0xF9A0` | 53 | UnwindData |  |
| 37 | `??0CVar@@QEAA@FH@Z` | `0xF9E0` | 53 | UnwindData |  |
| 38 | `??0CVar@@QEAA@G@Z` | `0xFA20` | 53 | UnwindData |  |
| 39 | `??0CVar@@QEAA@HPEAG@Z` | `0xFA60` | 61 | UnwindData |  |
| 40 | `??0CVar@@QEAA@HPEAUtagSAFEARRAY@@@Z` | `0xFAB0` | 75 | UnwindData |  |
| 41 | `??0CVar@@QEAA@HVauto_bstr@@@Z` | `0xFB10` | 106 | UnwindData |  |
| 42 | `??0CVar@@QEAA@J@Z` | `0xFB80` | 51 | UnwindData |  |
| 43 | `??0CVar@@QEAA@K@Z` | `0xFBC0` | 51 | UnwindData |  |
| 44 | `??0CVar@@QEAA@M@Z` | `0xFC00` | 55 | UnwindData |  |
| 45 | `??0CVar@@QEAA@N@Z` | `0xFC40` | 55 | UnwindData |  |
| 46 | `??0CVar@@QEAA@PEADH@Z` | `0xFC80` | 77 | UnwindData |  |
| 47 | `??0CVar@@QEAA@PEAGH@Z` | `0xFCE0` | 77 | UnwindData |  |
| 48 | `??0CVar@@QEAA@PEAU_FILETIME@@@Z` | `0xFD40` | 56 | UnwindData |  |
| 49 | `??0CVar@@QEAA@PEAU_GUID@@H@Z` | `0xFD80` | 77 | UnwindData |  |
| 50 | `??0CVar@@QEAA@PEAUtagBLOB@@H@Z` | `0xFDE0` | 77 | UnwindData |  |
| 51 | `??0CVar@@QEAA@PEAUtagVARIANT@@@Z` | `0xFE40` | 64 | UnwindData |  |
| 52 | `??0CVar@@QEAA@PEAVCVarVector@@H@Z` | `0xFE90` | 77 | UnwindData |  |
| 53 | `??0CVar@@QEAA@XZ` | `0xFEF0` | 31 | UnwindData |  |
| 55 | `??0CWbemInterval@@QEAA@XZ` | `0xFF20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??0CWbemTime@@IEAA@_J@Z` | `0xFF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??0CWbemTime@@QEAA@AEBV0@@Z` | `0xFF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??4CInCritSec@@QEAAAEAV0@AEBV0@@Z` | `0xFF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `??4CWbemTimeSpan@@QEAAAEAV0@$$QEAV0@@Z` | `0xFF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `??4CWbemTimeSpan@@QEAAAEAV0@AEBV0@@Z` | `0xFF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??0CWbemTime@@QEAA@XZ` | `0xFF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `?GetZero@CWbemTime@@SA?AV1@XZ` | `0xFF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `??0WString@@QEAA@AEBV0@@Z` | `0xFF70` | 35 | UnwindData |  |
| 62 | `??1CBaseAce@@UEAA@XZ` | `0xFFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `??1CCheckedInCritSec@@QEAA@XZ` | `0xFFC0` | 16 | UnwindData |  |
| 64 | `??1CCritSec@@QEAA@XZ` | `0xFFE0` | 23 | UnwindData |  |
| 65 | `??1CEnterWbemCriticalSection@@QEAA@XZ` | `0x10000` | 32 | UnwindData |  |
| 66 | `??1CEventLogRecord@@QEAA@XZ` | `0x10030` | 29 | UnwindData |  |
| 68 | `??1CInsertionString@@QEAA@XZ` | `0x10060` | 35 | UnwindData |  |
| 69 | `??1CUnkInternal@@UEAA@XZ` | `0x10090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `??1WString@@QEAA@XZ` | `0x100B0` | 26 | UnwindData |  |
| 72 | `??4C9XAce@@QEAAAEAV0@AEBV0@@Z` | `0x100F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `??4CCheckedInCritSec@@QEAAAEAV0@AEBV0@@Z` | `0x10120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `??4CEnterWbemCriticalSection@@QEAAAEAV0@AEBV0@@Z` | `0x10120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `??4CSmallArrayBlob@@QEAAAEAV0@AEBV0@@Z` | `0x10120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `??4CCircularQueue@@QEAAAEAV0@$$QEAV0@@Z` | `0x10140` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `??4CCircularQueue@@QEAAAEAV0@AEBV0@@Z` | `0x101A0` | 30 | UnwindData |  |
| 79 | `??4CContainerControl@@QEAAAEAV0@$$QEAV0@@Z` | `0x101D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `??4CContainerControl@@QEAAAEAV0@AEBV0@@Z` | `0x101D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `??4CCritSec@@QEAAAEAV0@AEBV0@@Z` | `0x101F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `??4CFlexQueue@@QEAAAEAV0@AEBV0@@Z` | `0x10220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `??4CWbemCriticalSection@@QEAAAEAV0@AEBV0@@Z` | `0x10220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `??4Registry@@QEAAAEAV0@AEBV0@@Z` | `0x10220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `??4CHaltable@@QEAAAEAV0@AEBV0@@Z` | `0x10240` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `??4CHex@@QEAAAEAV0@$$QEAV0@@Z` | `0x10280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `??4CHex@@QEAAAEAV0@AEBV0@@Z` | `0x10280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `??4CWbemInterval@@QEAAAEAV0@$$QEAV0@@Z` | `0x10280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `??4CWbemInterval@@QEAAAEAV0@AEBV0@@Z` | `0x10280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `??4CInsertionString@@QEAAAEAV0@$$QEAV0@@Z` | `0x10290` | 43 | UnwindData |  |
| 89 | `??4CInsertionString@@QEAAAEAV0@AEBV0@@Z` | `0x10290` | 43 | UnwindData |  |
| 92 | `??4CMemoryLog@@QEAAAEAV0@$$QEAV0@@Z` | `0x102D0` | 54 | UnwindData |  |
| 93 | `??4CMemoryLog@@QEAAAEAV0@AEBV0@@Z` | `0x10310` | 30 | UnwindData |  |
| 98 | `??4CSmallArrayBlob@@QEAAAEAV0@$$QEAV0@@Z` | `0x10340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `??4CStaticCritSec@@QEAAAEAV0@AEBV0@@Z` | `0x10360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `??4CTraceSessionControl@@QEAAAEAV0@$$QEAV0@@Z` | `0x10390` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `??4CTraceSessionControl@@QEAAAEAV0@AEBV0@@Z` | `0x103C0` | 30 | UnwindData |  |
| 103 | `??4CUnk@@QEAAAEAV0@AEBV0@@Z` | `0x103F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `??4CUnkInternal@@QEAAAEAV0@AEBV0@@Z` | `0x10420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `??4CWMITraceSettings@@QEAAAEAV0@$$QEAV0@@Z` | `0x10440` | 48 | UnwindData |  |
| 106 | `??4CWMITraceSettings@@QEAAAEAV0@AEBV0@@Z` | `0x10480` | 30 | UnwindData |  |
| 110 | `??4CWbemTime@@QEAAXAEBV0@@Z` | `0x104B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `??ACSmallArrayBlob@@QEBAPEAXH@Z` | `0x104C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `?GetAt@CSmallArrayBlob@@QEBAPEAXH@Z` | `0x104C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `??ACWStringArray@@QEBAPEAGH@Z` | `0x104D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `?GetAt@CWStringArray@@QEBAPEAGH@Z` | `0x104D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `??BCHex@@QEAAJXZ` | `0x104F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `?GetLockCount@CWbemCriticalSection@@QEAAJXZ` | `0x104F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `?GetMilliseconds@CWbemInterval@@QEBAKXZ` | `0x104F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `?GetType@CVar@@QEAAHXZ` | `0x104F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `?GetType@CVarVector@@QEAAHXZ` | `0x104F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `?IsEmpty@CInsertionString@@QEAAHXZ` | `0x104F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `?Size@CFlexArray@@QEBAHXZ` | `0x104F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `?Size@CSmallArrayBlob@@QEBAHXZ` | `0x104F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `?Size@CWStringArray@@QEBAHXZ` | `0x104F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `??BCVar@@QEAA?AU_FILETIME@@XZ` | `0x10500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `?GetFileTime@CVar@@QEAA?AU_FILETIME@@XZ` | `0x10500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `??BCVar@@QEAADXZ` | `0x10520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `??BCVar@@QEAAEXZ` | `0x10520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `?GetByte@CVar@@QEAAEXZ` | `0x10520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `?GetChar@CVar@@QEAADXZ` | `0x10520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `??BCVar@@QEAAFXZ` | `0x10530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `??BCVar@@QEAAGXZ` | `0x10530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `?GetBool@CVar@@QEAAFXZ` | `0x10530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `?GetShort@CVar@@QEAAFXZ` | `0x10530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `?GetWord@CVar@@QEAAGXZ` | `0x10530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `??BCVar@@QEAAJXZ` | `0x10540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `??BCVar@@QEAAKXZ` | `0x10540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `?GetDWORD@CVar@@QEAAKXZ` | `0x10540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `?GetLong@CVar@@QEAAJXZ` | `0x10540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `?GetOwningThreadId@CWbemCriticalSection@@QEAAKXZ` | `0x10540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `?GetStatus@CNtAcl@@QEAAKXZ` | `0x10540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `?GetStatus@CNtSecurityDescriptor@@QEAAKXZ` | `0x10540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `?GetStatus@CNtSid@@QEAAKXZ` | `0x10540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `?IsEntered@CCheckedInCritSec@@QEAAHXZ` | `0x10540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `?IsEntered@CEnterWbemCriticalSection@@QEAAHXZ` | `0x10540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `??BCVar@@QEAAMXZ` | `0x10550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `?GetFloat@CVar@@QEAAMXZ` | `0x10550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `??BCVar@@QEAANXZ` | `0x10560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `?GetDouble@CVar@@QEAANXZ` | `0x10560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `??BCVar@@QEAAPEADXZ` | `0x10570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `??BCVar@@QEAAPEAGXZ` | `0x10570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `??BCVar@@QEAAPEAU_GUID@@XZ` | `0x10570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `??BCVar@@QEAAPEAVCVarVector@@XZ` | `0x10570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `?GetClsId@CVar@@QEAAPEAU_GUID@@XZ` | `0x10570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `?GetLPSTR@CVar@@QEAAPEADXZ` | `0x10570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `?GetLPWSTR@CVar@@QEAAPEAGXZ` | `0x10570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `?GetPtr@CNtAce@@QEAAPEAU_ACCESS_ALLOWED_ACE@@XZ` | `0x10570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `?GetString@CInsertionString@@QEAAPEBGXZ` | `0x10570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `?GetVarVector@CVar@@QEAAPEAVCVarVector@@XZ` | `0x10570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `??BCVar@@QEAAPEAUtagBLOB@@XZ` | `0x10580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `?GetArrayPtr@CSmallArrayBlob@@QEAAPEAPEAXXZ` | `0x10580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `?GetArrayPtr@CSmallArrayBlob@@QEBAPEBQEAXXZ` | `0x10580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `?GetBlob@CVar@@QEAAPEAUtagBLOB@@XZ` | `0x10580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `?GetEventTraceProperties@CWMITraceSettings@@QEAAPEAU_EVENT_TRACE_PROPERTIES@@XZ` | `0x10580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `?GetRawData@CVar@@QEAAPEAXXZ` | `0x10580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `??BWString@@QEAAPEAGXZ` | `0x10590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `??BWString@@QEBAPEBGXZ` | `0x10590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `?Get100nss@CWbemTime@@QEBA_JXZ` | `0x10590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `?GetPtr@CNtAcl@@QEAAPEAU_ACL@@XZ` | `0x10590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `?GetPtr@CNtSecurityDescriptor@@QEAAPEAXXZ` | `0x10590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `?GetPtr@CNtSid@@QEAAPEAXXZ` | `0x10590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `??DCWbemInterval@@QEBA?AV0@N@Z` | `0x105A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `??GCWbemTime@@QEBA?AVCWbemInterval@@AEBV0@@Z` | `0x105C0` | 40 | UnwindData |  |
| 138 | `??HCWbemInterval@@QEBA?AV0@V0@@Z` | `0x105F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `??MCWbemInterval@@QEAAHV0@@Z` | `0x10610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `??MCWbemTime@@QEBAHAEBV0@@Z` | `0x10620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `??MWString@@QEBAHPEBG@Z` | `0x10640` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `??NCWbemTime@@QEBAHAEBV0@@Z` | `0x10670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `??NWString@@QEBAHPEBG@Z` | `0x10690` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `??OCWbemInterval@@QEAAHV0@@Z` | `0x106C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `??OCWbemTime@@QEBAHAEBV0@@Z` | `0x106D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `??OWString@@QEBAHPEBG@Z` | `0x106F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `??PCWbemTime@@QEBAHAEBV0@@Z` | `0x10720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `??PWString@@QEBAHPEBG@Z` | `0x10740` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `??YCWbemInterval@@QEAAXV0@@Z` | `0x10770` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `??_FCEventLog@@QEAAXXZ` | `0x10AC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `??_FCFlexArray@@QEAAXXZ` | `0x10AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `??_FCFlexQueue@@QEAAXXZ` | `0x10B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `??_FCNtAcl@@QEAAXXZ` | `0x10B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `??_FCUnk@@QEAAXXZ` | `0x10B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `??_FCWStringArray@@QEAAXXZ` | `0x10B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `?Access@CSafeArray@@QEAAJPEAPEAX@Z` | `0x10B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `?Add@CFlexArray@@QEAAHPEAX@Z` | `0x10BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `?AddBool@CSafeArray@@QEAAHF@Z` | `0x10BD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `?AddShort@CSafeArray@@QEAAHF@Z` | `0x10BD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `?AddByte@CSafeArray@@QEAAHE@Z` | `0x10C00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `?AddDouble@CSafeArray@@QEAAHN@Z` | `0x10C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `?AddFloat@CSafeArray@@QEAAHM@Z` | `0x10C50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `?AddLong@CSafeArray@@QEAAHJ@Z` | `0x10C80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `?AddRef@CContainerControl@@UEAAXPEAUIUnknown@@@Z` | `0x10CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `?AddRef@CUnkInternal@@UEAAKXZ` | `0x10CD0` | 51 | UnwindData |  |
| 177 | `?BindPtr@WString@@QEAAXPEAG@Z` | `0x10D10` | 46 | UnwindData |  |
| 178 | `?CanDelete@CVar@@QEAAHXZ` | `0x10D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `?Compress@CWStringArray@@QEAAXXZ` | `0x10D60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `?DecrementIndex@CFlexQueue@@IEAAXAEAH@Z` | `0x10D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `?ElementSize@CSafeArray@@QEAAHXZ` | `0x10DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `?GetFlags@C9XAce@@UEAAHXZ` | `0x10DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `?GetLastError@Registry@@QEAAJXZ` | `0x10DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `?Enter@CCheckedInCritSec@@QEAAXXZ` | `0x10DC0` | 37 | UnwindData |  |
| 184 | `?Enter@CCritSec@@QEAAXXZ` | `0x10DF0` | 24 | UnwindData |  |
| 185 | `?Equal@WString@@QEBAHPEBG@Z` | `0x10E10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `?EqualNoCase@WString@@QEBAHPEBG@Z` | `0x10E40` | 27 | UnwindData |  |
| 189 | `?GetAccessMask@C9XAce@@UEAAKXZ` | `0x10E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `?GetStatus@CNtAce@@UEAAKXZ` | `0x10E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `?GetType@CSafeArray@@QEAAHXZ` | `0x10E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `?GetAreaFlags@CWMITraceSettings@@QEAAKXZ` | `0x10EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `?GetRecursionCount@CWbemCriticalSection@@QEAAJXZ` | `0x10EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `?GetArray@CSafeArray@@QEAAPEAUtagSAFEARRAY@@XZ` | `0x10EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `?GetArrayPtr@CFlexArray@@QEAAPEAPEAXXZ` | `0x10EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `?GetArrayPtr@CFlexArray@@QEBAPEBQEAXXZ` | `0x10EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `?GetArrayPtr@CWStringArray@@QEAAPEAPEBGXZ` | `0x10EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `?GetBoolAt@CSafeArray@@QEAAFH@Z` | `0x10ED0` | 33 | UnwindData |  |
| 239 | `?GetShortAt@CSafeArray@@QEAAFH@Z` | `0x10ED0` | 33 | UnwindData |  |
| 203 | `?GetByteAt@CSafeArray@@QEAAEH@Z` | `0x10F00` | 32 | UnwindData |  |
| 206 | `?GetCreationTime@CEventLogRecord@@QEAA?AVCWbemTime@@XZ` | `0x10F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `?GetDispatch@CVar@@QEAAPEAUIDispatch@@XZ` | `0x10F50` | 41 | UnwindData |  |
| 255 | `?GetUnknown@CVar@@QEAAPEAUIUnknown@@XZ` | `0x10F50` | 41 | UnwindData |  |
| 210 | `?GetDoubleAt@CSafeArray@@QEAANH@Z` | `0x10F80` | 34 | UnwindData |  |
| 211 | `?GetEmbeddedObject@CVar@@QEAAPEAUIUnknown@@XZ` | `0x10FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `?GetFloatAt@CSafeArray@@QEAAMH@Z` | `0x10FC0` | 34 | UnwindData |  |
| 217 | `?GetInfinity@CWbemInterval@@SA?AV1@XZ` | `0x10FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `?GetInfinity@CWbemTime@@SA?AV1@XZ` | `0x11000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `?GetLongAt@CSafeArray@@QEAAJH@Z` | `0x11020` | 32 | UnwindData |  |
| 227 | `?GetNumStrings@CEventLogRecord@@QEAAGXZ` | `0x11050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `?GetQueueSize@CFlexQueue@@QEBAHXZ` | `0x11060` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `?GetSeconds@CWbemInterval@@QEBAKXZ` | `0x11090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `?GetSessionName@CWMITraceSettings@@QEAAPEAGXZ` | `0x110B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `?GetSize@CNtAce@@QEAAKXZ` | `0x110C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `?GetTraceLevel@CWMITraceSettings@@QEAAEXZ` | `0x110E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `?IsEnabled@CTraceSessionControl@@QEAA_NXZ` | `0x110E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `?GetType@C9XAce@@UEAAHXZ` | `0x110F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `?Status@CVar@@QEAAHXZ` | `0x110F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `?GetUnknown@CUnk@@QEAAPEAUIUnknown@@XZ` | `0x11100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `?IncrementIndex@CFlexQueue@@IEAAXAEAH@Z` | `0x11120` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `?InternalQueryInterface@CUnkInternal@@QEAAJAEBU_GUID@@PEAPEAX@Z` | `0x111E0` | 74 | UnwindData |  |
| 262 | `?InternalRelease@CUnkInternal@@QEAAKXZ` | `0x11230` | 48 | UnwindData |  |
| 267 | `?IsFinite@CWbemInterval@@QEBAHXZ` | `0x11270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `?IsFinite@CWbemTime@@QEBAHXZ` | `0x11280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `?IsNull@CVar@@QEAAHXZ` | `0x112A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `?IsOptimized@CVarVector@@QEAAHXZ` | `0x112B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `?IsUser@CNtSid@@QEAA_NXZ` | `0x112D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `?IsValid@CNtAcl@@QEAAHXZ` | `0x112E0` | 126 | UnwindData |  |
| 274 | `?IsValid@CNtSecurityDescriptor@@QEAAHXZ` | `0x11370` | 126 | UnwindData |  |
| 275 | `?IsValid@CNtSid@@QEAAHXZ` | `0x11400` | 126 | UnwindData |  |
| 276 | `?IsZero@CWbemInterval@@QEBAHXZ` | `0x11490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `?IsZero@CWbemTime@@QEBAHXZ` | `0x114A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `?Leave@CCheckedInCritSec@@QEAAXXZ` | `0x114B0` | 41 | UnwindData |  |
| 279 | `?Leave@CCritSec@@QEAAXXZ` | `0x114E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `?Length@WString@@QEBAHXZ` | `0x11500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `?ObjectCreated@CContainerControl@@UEAAHPEAUIUnknown@@@Z` | `0x11520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `?OnInitialize@CUnk@@UEAAHXZ` | `0x11520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `?QueryInterface@CUnkInternal@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x11540` | 53 | UnwindData |  |
| 288 | `?Release@CContainerControl@@UEAAXPEAUIUnknown@@@Z` | `0x11580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `?Release@CUnkInternal@@UEAAKXZ` | `0x115A0` | 71 | UnwindData |  |
| 291 | `?Set100nss@CWbemTime@@QEAAX_J@Z` | `0x115F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `?SetAreaFlags@CWMITraceSettings@@QEAAXK@Z` | `0x11600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `?SetDestructorPolicy@CSafeArray@@QEAAXH@Z` | `0x11600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `?SetAsNull@CVar@@QEAAXXZ` | `0x11610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `?SetBool@CVar@@QEAAXF@Z` | `0x11630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `?SetBoolAt@CSafeArray@@QEAAHHF@Z` | `0x11650` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `?SetShortAt@CSafeArray@@QEAAHHF@Z` | `0x11650` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `?SetByte@CVar@@QEAAXE@Z` | `0x11680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `?SetByteAt@CSafeArray@@QEAAHHE@Z` | `0x116A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `?SetCanDelete@CVar@@QEAAXH@Z` | `0x116D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `?SetChar@CVar@@QEAAXD@Z` | `0x116E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `?SetDWORD@CVar@@QEAAXK@Z` | `0x11700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `?SetDouble@CVar@@QEAAXN@Z` | `0x11720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `?SetDoubleAt@CSafeArray@@QEAAHHN@Z` | `0x11740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `?SetEmbeddedObject@CVar@@QEAAXPEAUIUnknown@@@Z` | `0x11760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `?SetFileTime@CVar@@QEAAXPEAU_FILETIME@@@Z` | `0x11780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `?SetFlags@C9XAce@@UEAAXJ@Z` | `0x117A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `?SetFlags@CNtAce@@UEAAXJ@Z` | `0x117B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `?SetFloat@CVar@@QEAAXM@Z` | `0x117C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `?SetFloatAt@CSafeArray@@QEAAHHM@Z` | `0x117E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `?SetGrowGranularity@CSafeArray@@QEAAXH@Z` | `0x11810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `?SetLong@CVar@@QEAAXJ@Z` | `0x11820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `?SetLongAt@CSafeArray@@QEAAHHJ@Z` | `0x11840` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `?SetMilliseconds@CWbemInterval@@QEAAXK@Z` | `0x11870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `?SetRawArrayMaxElement@CSafeArray@@QEAAXH@Z` | `0x11870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `?SetSize@CFlexArray@@QEAAXH@Z` | `0x11870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `?SetShort@CVar@@QEAAXF@Z` | `0x11880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `?SetTraceLevel@CWMITraceSettings@@QEAAXE@Z` | `0x118A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `?SetWord@CVar@@QEAAXG@Z` | `0x118B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `?Size@CSafeArray@@QEAAHXZ` | `0x118D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `?Status@CSafeArray@@QEAAHXZ` | `0x118E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `?Status@CVarVector@@QEAAHXZ` | `0x118F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `?Unaccess@CSafeArray@@QEAAJXZ` | `0x11930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `?Unqueue@CFlexQueue@@QEAAPEAXXZ` | `0x11950` | 60 | UnwindData |  |
| 330 | `?isValid@CHaltable@@QEAA_NXZ` | `0x11C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `GetSystemEventsForShutdown` | `0x11C80` | 959 | UnwindData |  |
| 281 | `MoveToAlone` | `0x15410` | 1,303 | UnwindData |  |
| 282 | `MoveToShared` | `0x15930` | 1,054 | UnwindData |  |
| 331 | `DllRegisterServer` | `0x15FE0` | 2,745 | UnwindData |  |
| 332 | `DllUnregisterServer` | `0x16AA0` | 318 | UnwindData |  |
| 181 | `DredgeRA` | `0x16BF0` | 53,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `??_7CWin32DefaultArena@@6B@` | `0x23CA0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `??_7CArena@@6B@` | `0x23CB8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `??_7CUnkInternal@@6B@` | `0x23CD0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `??_7CUnk@@6B@` | `0x23CF8` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `??_7CContainerControl@@6B@` | `0x23D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `??_7CLifeControl@@6B@` | `0x23D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `??_7CHaltable@@6B@` | `0x23D70` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `??_7C9XAce@@6B@` | `0x23D78` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `??_7CNtAce@@6B@` | `0x23DC0` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `??_7CBaseAce@@6B@` | `0x23E08` | 0 | Indeterminate |  |
