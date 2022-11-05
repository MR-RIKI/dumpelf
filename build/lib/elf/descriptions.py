"""
  Copyright (C) 2008-2013  Tomasz Bursztyka

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as published
  by the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU Lesser General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

""" Human readable descriptions of all identifiers """

desc_ehdr_class = {
    'ELFCLASSNONE' : 'Invalid class',
    'ELFCLASS32'   : '32-bit objects',
    'ELFCLASS64'   : '64-bit objects',
    'ELFCLASSNUM'  : 'No description',
    }

desc_ehdr_osabi = {
    'ELFOSABI_NONE'       : 'UNIX System V ABI',
    'ELFOSABI_SYSV'       : 'Alias.',
    'ELFOSABI_HPUX'       : 'HP-UX',
    'ELFOSABI_NETBSD'     : 'NetBSD.',
    'ELFOSABI_LINUX'      : 'Linux.',
    'ELFOSABI_SOLARIS'    : 'Sun Solaris.',
    'ELFOSABI_AIX'        : 'IBM AIX.',
    'ELFOSABI_IRIX'       : 'SGI Irix.',
    'ELFOSABI_FREEBSD'    : 'FreeBSD.',
    'ELFOSABI_TRU64'      : 'Compaq TRU64 UNIX.',
    'ELFOSABI_MODESTO'    : 'Novell Modesto.',
    'ELFOSABI_OPENBSD'    : 'OpenBSD.',
    'ELFOSABI_ARM'        : 'ARM',
    'ELFOSABI_STANDALONE' : 'Standalone (embedded) application',
    }

desc_ehdr_type = {
    'ET_NONE'   : 'No file type',
    'ET_REL'    : 'Relocatable file',
    'ET_EXEC'   : 'Executable file',
    'ET_DYN'    : 'Shared object file',
    'ET_CORE'   : 'Core file',
    'ET_NUM'    : 'Number of defined types',
    'ET_LOOS'   : 'OS-specific range start',
    'ET_HIOS'   : 'OS-specific range end',
    'ET_LOPROC' : 'Processor-specific range start',
    'ET_HIPROC' : 'Processor-specific range end',
    }

desc_ehdr_machine = {
    'EM_NONE'        : 'No machine',
    'EM_M32'         : 'AT&T WE 32100',
    'EM_SPARC'       : 'SUN SPARC',
    'EM_386'         : 'Intel 80386',
    'EM_68K'         : 'Motorola m68k family',
    'EM_88K'         : 'Motorola m88k family',
    'EM_860'         : 'Intel 80860',
    'EM_MIPS'        : 'MIPS R3000 big-endian',
    'EM_S370'        : 'IBM System/370',
    'EM_MIPS_RS3_LE' : 'MIPS R3000 little-endian',
    'EM_PARISC'      : 'HPPA',
    'EM_VPP500'      : 'Fujitsu VPP500',
    'EM_SPARC32PLUS' : 'Sun\'s "v8plus"',
    'EM_960'         : 'Intel 80960',
    'EM_PPC'         : 'PowerPC',
    'EM_PPC64'       : 'PowerPC 64-bit',
    'EM_S390'        : 'IBM S390',
    'EM_V800'        : 'NEC V800 series',
    'EM_FR20'        : 'Fujitsu FR20',
    'EM_RH32'        : 'TRW RH-32',
    'EM_RCE'         : 'Motorola RCE',
    'EM_ARM'         : 'ARM',
    'EM_FAKE_ALPHA'  : 'Digital Alpha',
    'EM_SH'          : 'Hitachi SH',
    'EM_SPARCV9'     : 'SPARC v9 64-bit',
    'EM_TRICORE'     : 'Siemens Tricore',
    'EM_ARC'         : 'Argonaut RISC Core',
    'EM_H8_300'      : 'Hitachi H8/300',
    'EM_H8_300H'     : 'Hitachi H8/300H',
    'EM_H8S'         : 'Hitachi H8S',
    'EM_H8_500'      : 'Hitachi H8/500',
    'EM_IA_64'       : 'Intel Merced',
    'EM_MIPS_X'      : 'Stanford MIPS-X',
    'EM_COLDFIRE'    : 'Motorola Coldfire',
    'EM_68HC12'      : 'Motorola M68HC12',
    'EM_MMA'         : 'Fujitsu MMA Multimedia Accelerator',
    'EM_PCP'         : 'Siemens PCP',
    'EM_NCPU'        : 'Sony nCPU embeeded RISC',
    'EM_NDR1'        : 'Denso NDR1 microprocessor',
    'EM_STARCORE'    : 'Motorola Start*Core processor',
    'EM_ME16'        : 'Toyota ME16 processor',
    'EM_ST100'       : 'STMicroelectronic ST100 processor',
    'EM_TINYJ'       : 'Advanced Logic Corp. Tinyj emb.fam',
    'EM_X86_64'      : 'AMD x86-64 architecture',
    'EM_PDSP'        : 'Sony DSP Processor',
    'EM_FX66'        : 'Siemens FX66 microcontroller',
    'EM_ST9PLUS'     : 'STMicroelectronics ST9+ 8/16 mc',
    'EM_ST7'         : 'STmicroelectronics ST7 8 bit mc',
    'EM_68HC16'      : 'Motorola MC68HC16 microcontroller',
    'EM_68HC11'      : 'Motorola MC68HC11 microcontroller',
    'EM_68HC08'      : 'Motorola MC68HC08 microcontroller',
    'EM_68HC05'      : 'Motorola MC68HC05 microcontroller',
    'EM_SVX'         : 'Silicon Graphics SVx',
    'EM_ST19'        : 'STMicroelectronics ST19 8 bit mc',
    'EM_VAX'         : 'Digital VAX',
    'EM_CRIS'        : 'Axis Communications 32-bit embedded processor',
    'EM_JAVELIN'     : 'Infineon Technologies 32-bit embedded processor',
    'EM_FIREPATH'    : 'Element 14 64-bit DSP Processor',
    'EM_ZSP'         : 'LSI Logic 16-bit DSP Processor',
    'EM_MMIX'        : 'Donald Knuth\'s educational 64-bit processor',
    'EM_HUANY'       : 'Harvard University machine-independent object files',
    'EM_PRISM'       : 'SiTera Prism',
    'EM_AVR'         : 'Atmel AVR 8-bit microcontroller',
    'EM_FR30'        : 'Fujitsu FR30',
    'EM_D10V'        : 'Mitsubishi D10V',
    'EM_D30V'        : 'Mitsubishi D30V',
    'EM_V850'        : 'NEC v850',
    'EM_M32R'        : 'Mitsubishi M32R',
    'EM_MN10300'     : 'Matsushita MN10300',
    'EM_MN10200'     : 'Matsushita MN10200',
    'EM_PJ'          : 'picoJava',
    'EM_OPENRISC'    : 'OpenRISC 32-bit embedded processor',
    'EM_ARC_A5'      : 'ARC Cores Tangent-A5',
    'EM_XTENSA'      : 'Tensilica Xtensa Architecture',
    'EM_NUM'         : 'No description',
    'EM_ALPHA'       : 'No description',
    }

desc_ehdr_version = {
    'EV_NONE'    : 'Invalid ELF version',
    'EV_CURRENT' : 'Current version',
    'EV_NUM'     : 'No description',
    }

desc_shdr_index = {
    'SHN_UNDEF'              : 'Undefined section',
    'SHN_LORESERVE'          : 'Start of reserved indices',
    'SHN_LOPROC'             : 'Start of processor-specific',
    'SHN_BEFORE'             : 'Order section before all others(Solaris).',
    'SHN_AFTER'              : 'Order section after all others(Solaris).',
    'SHN_HIPROC'             : 'End of processor-specific',
    'SHN_LOOS'               : 'Start of OS-specific',
    'SHN_HIOS'               : 'End of OS-specific',
    'SHN_ABS'                : 'Associated symbol is absolute',
    'SHN_COMMON'             : 'Associated symbol is common',
    'SHN_XINDEX'             : 'Index is in extra table.',
    'SHN_HIRESERVE'          : 'End of reserved indices',
    'SHN_MIPS_ACOMMON'       : 'Allocated common symbols',
    'SHN_MIPS_TEXT'          : 'Allocated test symbols.',
    'SHN_MIPS_DATA'          : 'Allocated data symbols.',
    'SHN_MIPS_SCOMMON'       : 'Small common symbols',
    'SHN_MIPS_SUNDEFINED'    : 'Small undefined symbols',
    'SHN_PARISC_ANSI_COMMON' : 'Section for tenatively declaredsymbols in ANSI C.',
    'SHN_PARISC_HUGE_COMMON' : 'Common blocks in huge model.',
    }

desc_shdr_type = {
    'SHT_NULL'               : 'Section header table entry unused',
    'SHT_PROGBITS'           : 'Program data',
    'SHT_SYMTAB'             : 'Symbol table',
    'SHT_STRTAB'             : 'String table',
    'SHT_RELA'               : 'Relocation entries with addends',
    'SHT_HASH'               : 'Symbol hash table',
    'SHT_DYNAMIC'            : 'Dynamic linking information',
    'SHT_NOTE'               : 'Notes',
    'SHT_NOBITS'             : 'Program space with no data (bss)',
    'SHT_REL'                : 'Relocation entries, no addends',
    'SHT_SHLIB'              : 'Reserved',
    'SHT_DYNSYM'             : 'Dynamic linker symbol table',
    'SHT_INIT_ARRAY'         : 'Array of constructors',
    'SHT_FINI_ARRAY'         : 'Array of destructors',
    'SHT_PREINIT_ARRAY'      : 'Array of pre-constructors',
    'SHT_GROUP'              : 'Section group',
    'SHT_SYMTAB_SHNDX'       : 'Extended section indeces',
    'SHT_NUM'                : 'Number of defined types.',
    'SHT_LOOS'               : 'Start OS-specific.',
    'SHT_GNU_HASH'           : 'GNU-style hash table.',
    'SHT_GNU_LIBLIST'        : 'Prelink library list',
    'SHT_CHECKSUM'           : 'Checksum for DSO content.',
    'SHT_LOSUNW'             : 'Sun-specific low bound.',
    'SHT_SUNW_move'          : 'No description',
    'SHT_SUNW_COMDAT'        : 'No description',
    'SHT_SUNW_syminfo'       : 'No description',
    'SHT_GNU_verdef'         : 'Version definition section.',
    'SHT_GNU_verneed'        : 'Version needs section.',
    'SHT_GNU_versym'         : 'Version symbol table.',
    'SHT_HISUNW'             : 'Sun-specific high bound.',
    'SHT_HIOS'               : 'End OS-specific type',
    'SHT_LOPROC'             : 'Start of processor-specific',
    'SHT_HIPROC'             : 'End of processor-specific',
    'SHT_LOUSER'             : 'Start of application-specific',
    'SHT_HIUSER'             : 'End of application-specific',
    'SHT_MIPS_LIBLIST'       : 'Shared objects used in link',
    'SHT_MIPS_MSYM'          : 'No description',
    'SHT_MIPS_CONFLICT'      : 'Conflicting symbols',
    'SHT_MIPS_GPTAB'         : 'Global data area sizes',
    'SHT_MIPS_UCODE'         : 'Reserved for SGI/MIPS compilers',
    'SHT_MIPS_DEBUG'         : 'MIPS ECOFF debugging information',
    'SHT_MIPS_REGINFO'       : 'Register usage information',
    'SHT_MIPS_PACKAGE'       : 'No description',
    'SHT_MIPS_PACKSYM'       : 'No description',
    'SHT_MIPS_RELD'          : 'No description',
    'SHT_MIPS_IFACE'         : 'No description',
    'SHT_MIPS_CONTENT'       : 'No description',
    'SHT_MIPS_OPTIONS'       : 'Miscellaneous options.',
    'SHT_MIPS_SHDR'          : 'No description',
    'SHT_MIPS_FDESC'         : 'No description',
    'SHT_MIPS_EXTSYM'        : 'No description',
    'SHT_MIPS_DENSE'         : 'No description',
    'SHT_MIPS_PDESC'         : 'No description',
    'SHT_MIPS_LOCSYM'        : 'No description',
    'SHT_MIPS_AUXSYM'        : 'No description',
    'SHT_MIPS_OPTSYM'        : 'No description',
    'SHT_MIPS_LOCSTR'        : 'No description',
    'SHT_MIPS_LINE'          : 'No description',
    'SHT_MIPS_RFDESC'        : 'No description',
    'SHT_MIPS_DELTASYM'      : 'No description',
    'SHT_MIPS_DELTAINST'     : 'No description',
    'SHT_MIPS_DELTACLASS'    : 'No description',
    'SHT_MIPS_DWARF'         : 'DWARF debugging information.',
    'SHT_MIPS_DELTADECL'     : 'No description',
    'SHT_MIPS_SYMBOL_LIB'    : 'No description',
    'SHT_MIPS_EVENTS'        : 'Event section.',
    'SHT_MIPS_TRANSLATE'     : 'No description',
    'SHT_MIPS_PIXIE'         : 'No description',
    'SHT_MIPS_XLATE'         : 'No description',
    'SHT_MIPS_XLATE_DEBUG'   : 'No description',
    'SHT_MIPS_WHIRL'         : 'No description',
    'SHT_MIPS_EH_REGION'     : 'No description',
    'SHT_MIPS_XLATE_OLD'     : 'No description',
    'SHT_MIPS_PDR_EXCEPTION' : 'No description',
    'SHT_PARISC_EXT'         : 'Contains product specific ext.',
    'SHT_PARISC_UNWIND'      : 'Unwind information.',
    'SHT_PARISC_DOC'         : 'Debug info for optimized code.',
    'SHT_ALPHA_DEBUG'        : 'No description',
    'SHT_ALPHA_REGINFO'      : 'No description',
    'SHT_IA_64_EXT'          : 'extension bits',
    'SHT_IA_64_UNWIND'       : 'unwind bits',
    }

desc_shdr_flag = {
    'SHF_WRITE'            : 'Writable',
    'SHF_ALLOC'            : 'Occupies memory during execution',
    'SHF_EXECINSTR'        : 'Executable',
    'SHF_MERGE'            : 'Might be merged',
    'SHF_STRINGS'          : 'Contains nul-terminated strings',
    'SHF_INFO_LINK'        : '`sh_info\' contains SHT index',
    'SHF_LINK_ORDER'       : 'Preserve order after combining',
    'SHF_OS_NONCONFORMING' : 'Non-standard OS specific handlingrequired',
    'SHF_GROUP'            : 'Section is member of a group.',
    'SHF_TLS'              : 'Section hold thread-local data.',
    'SHF_MASKOS'           : 'OS-specific.',
    'SHF_MASKPROC'         : 'Processor-specific',
    'SHF_ORDERED'          : 'Special ordering requirement(Solaris).',
    'SHF_EXCLUDE'          : 'Section is excluded unlessreferenced or allocated (Solaris).',
    'SHF_MIPS_GPREL'       : 'Must be part of global data area',
    'SHF_MIPS_MERGE'       : 'No description',
    'SHF_MIPS_ADDR'        : 'No description',
    'SHF_MIPS_STRINGS'     : 'No description',
    'SHF_MIPS_NOSTRIP'     : 'No description',
    'SHF_MIPS_LOCAL'       : 'No description',
    'SHF_MIPS_NAMES'       : 'No description',
    'SHF_MIPS_NODUPE'      : 'No description',
    'SHF_PARISC_SHORT'     : 'Section with short addressing.',
    'SHF_PARISC_HUGE'      : 'Section far from gp.',
    'SHF_PARISC_SBP'       : 'Static branch prediction code.',
    'SHF_ALPHA_GPREL'      : 'No description',
    'SHF_ARM_ENTRYSECT'    : 'Section contains an entry point',
    'SHF_ARM_COMDEF'       : 'Section may be multiply definedin the input to a link step',
    'SHF_IA_64_SHORT'      : 'section near gp',
    'SHF_IA_64_NORECOV'    : 'spec insns w/o recovery',
    }

desc_symtab_bind = {
    'STB_LOCAL'             : 'Local symbol',
    'STB_GLOBAL'            : 'Global symbol',
    'STB_WEAK'              : 'Weak symbol',
    'STB_NUM'               : 'Number of defined types.',
    'STB_LOOS'              : 'Start of OS-specific',
    'STB_HIOS'              : 'End of OS-specific',
    'STB_LOPROC'            : 'Start of processor-specific',
    'STB_HIPROC'            : 'End of processor-specific',
    'STB_MIPS_SPLIT_COMMON' : 'No description',
    }

desc_symtab_type = {
    'STT_NOTYPE'           : 'Symbol type is unspecified',
    'STT_OBJECT'           : 'Symbol is a data object',
    'STT_FUNC'             : 'Symbol is a code object',
    'STT_SECTION'          : 'Symbol associated with a section',
    'STT_FILE'             : 'Symbol\'s name is file name',
    'STT_COMMON'           : 'Symbol is a common data object',
    'STT_TLS'              : 'Symbol is thread-local data object',
    'STT_NUM'              : 'Number of defined types.',
    'STT_LOOS'             : 'Start of OS-specific',
    'STT_HIOS'             : 'End of OS-specific',
    'STT_LOPROC'           : 'Start of processor-specific',
    'STT_HIPROC'           : 'End of processor-specific',
    'STT_SPARC_REGISTER'   : 'Global register reserved to app.',
    'STT_PARISC_MILLICODE' : 'Millicode function entry point.',
    'STT_HP_OPAQUE'        : 'No description',
    'STT_HP_STUB'          : 'No description',
    'STT_ARM_TFUNC'        : 'No description',
    }

desc_symtafb_visibility = {
    'STV_DEFAULT'   : 'Default symbol visibility rules',
    'STV_INTERNAL'  : 'Processor specific hidden class',
    'STV_HIDDEN'    : 'Sym unavailable in other modules',
    'STV_PROTECTED' : 'Not preemptible, not exported',
    }

desc_syminfo_boundto = {
    'SYMINFO_BT_SELF'       : 'Symbol bound to self',
    'SYMINFO_BT_PARENT'     : 'Symbol bound to parent',
    'SYMINFO_BT_LOWRESERVE' : 'Beginning of reserved entries',
    }

desc_syminfo_flag = {
    'SYMINFO_FLG_DIRECT'   : 'Direct bound symbol',
    'SYMINFO_FLG_PASSTHRU' : 'Pass-thru symbol for translator',
    'SYMINFO_FLG_COPY'     : 'Symbol is a copy-reloc',
    'SYMINFO_FLG_LAZYLOAD' : 'Symbol bound to object to be lazyloaded',
    }

desc_syminfo_version = {
    'SYMINFO_NONE'          : 'No description',
    'SYMINFO_CURRENT'       : 'No description',
    'SYMINFO_NUM'           : 'No description',
    }

desc_phdr_type = {
    'PT_NULL'              : 'Program header table entry unused',
    'PT_LOAD'              : 'Loadable program segment',
    'PT_DYNAMIC'           : 'Dynamic linking information',
    'PT_INTERP'            : 'Program interpreter',
    'PT_NOTE'              : 'Auxiliary information',
    'PT_SHLIB'             : 'Reserved',
    'PT_PHDR'              : 'Entry for header table itself',
    'PT_TLS'               : 'Thread-local storage segment',
    'PT_NUM'               : 'Number of defined types',
    'PT_LOOS'              : 'Start of OS-specific',
    'PT_GNU_EH_FRAME'      : 'GCC .eh_frame_hdr segment',
    'PT_GNU_STACK'         : 'Indicates stack executability',
    'PT_GNU_RELRO'         : 'Read-only after relocation',
    'PT_PAX_FLAGS'         : 'Indicates PaX flag markings',
    'PT_LOSUNW'            : 'No description',
    'PT_SUNWBSS'           : 'Sun Specific segment',
    'PT_SUNWSTACK'         : 'Stack segment',
    'PT_HISUNW'            : 'No description',
    'PT_HIOS'              : 'End of OS-specific',
    'PT_LOPROC'            : 'Start of processor-specific',
    'PT_HIPROC'            : 'End of processor-specific',
    'PT_MIPS_REGINFO'      : 'Register usage information',
    'PT_MIPS_RTPROC'       : 'Runtime procedure table.',
    'PT_MIPS_OPTIONS'      : 'No description',
    'PT_HP_TLS'            : 'No description',
    'PT_HP_CORE_NONE'      : 'No description',
    'PT_HP_CORE_VERSION'   : 'No description',
    'PT_HP_CORE_KERNEL'    : 'No description',
    'PT_HP_CORE_COMM'      : 'No description',
    'PT_HP_CORE_PROC'      : 'No description',
    'PT_HP_CORE_LOADABLE'  : 'No description',
    'PT_HP_CORE_STACK'     : 'No description',
    'PT_HP_CORE_SHM'       : 'No description',
    'PT_HP_CORE_MMF'       : 'No description',
    'PT_HP_PARALLEL'       : 'No description',
    'PT_HP_FASTBIND'       : 'No description',
    'PT_HP_OPT_ANNOT'      : 'No description',
    'PT_HP_HSL_ANNOT'      : 'No description',
    'PT_HP_STACK'          : 'No description',
    'PT_PARISC_ARCHEXT'    : 'No description',
    'PT_PARISC_UNWIND'     : 'No description',
    'PT_ARM_EXIDX'         : '.ARM.exidx segment',
    'PT_IA_64_ARCHEXT'     : 'arch extension bits',
    'PT_IA_64_UNWIND'      : 'ia64 unwind bits',
    'PT_IA_64_HP_OPT_ANOT' : 'No description',
    'PT_IA_64_HP_HSL_ANOT' : 'No description',
    'PT_IA_64_HP_STACK'    : 'No description',
    }

desc_phdr_flag = {
    'PF_X'              : 'Segment is executable',
    'PF_W'              : 'Segment is writable',
    'PF_R'              : 'Segment is readable',
    'PF_PAGEEXEC'       : 'Enable  PAGEEXEC',
    'PF_NOPAGEEXEC'     : 'Disable PAGEEXEC',
    'PF_SEGMEXEC'       : 'Enable  SEGMEXEC',
    'PF_NOSEGMEXEC'     : 'Disable SEGMEXEC',
    'PF_MPROTECT'       : 'Enable  MPROTECT',
    'PF_NOMPROTECT'     : 'Disable MPROTECT',
    'PF_RANDEXEC'       : 'Enable  RANDEXEC',
    'PF_NORANDEXEC'     : 'Disable RANDEXEC',
    'PF_EMUTRAMP'       : 'Enable  EMUTRAMP',
    'PF_NOEMUTRAMP'     : 'Disable EMUTRAMP',
    'PF_RANDMMAP'       : 'Enable  RANDMMAP',
    'PF_NORANDMMAP'     : 'Disable RANDMMAP',
    'PF_MASKOS'         : 'OS-specific',
    'PF_MASKPROC'       : 'Processor-specific',
    'PF_MIPS_LOCAL'     : 'No description',
    'PF_PARISC_SBP'     : 'No description',
    'PF_HP_PAGE_SIZE'   : 'No description',
    'PF_HP_FAR_SHARED'  : 'No description',
    'PF_HP_NEAR_SHARED' : 'No description',
    'PF_HP_CODE'        : 'No description',
    'PF_HP_MODIFY'      : 'No description',
    'PF_HP_LAZYSWAP'    : 'No description',
    'PF_HP_SBP'         : 'No description',
    'PF_ARM_SB'         : 'Segment contains the locationaddressed by the static base',
    'PF_IA_64_NORECOV'  : 'spec insns w/o recovery',
    }

desc_verdef_version = {
    'VER_DEF_NONE'    : 'No version',
    'VER_DEF_CURRENT' : 'Current version',
    'VER_DEF_NUM'     : 'Given version number',
    }

desc_verdef_flag = {
    'VER_FLG_BASE' : 'Version definition of file itself',
    'VER_FLG_WEAK' : 'Weak version identifier',
    'VER_FLG_WEAK' : 'Weak version identifier',
    }

desc_verdep_version = {
    'VER_NEED_NONE'    : 'No version',
    'VER_NEED_CURRENT' : 'Current version',
    'VER_NEED_NUM'     : 'Given version number',
    }

#######
# EOF #
#######

