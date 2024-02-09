import sqlite3
import streamlit as st


def create_database():
    conn = sqlite3.connect('amohsen.db')
    c = conn.cursor()
    c.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='students'
    """)
    if not c.fetchone():
        c.execute('''CREATE TABLE students (
                                       LastName TEXT,
                                       FirstName TEXT,
                                       StudentID TEXT PRIMARY KEY,
                                       Course TEXT,
                                       Program TEXT,
                                       ArtSchool TEXT,
                                       SubPlanText TEXT,
                                       FirstSemester TEXT,
                                       Catalog TEXT,
                                       HGHRcertCatalog TEXT,
                                       TranslCertCatalog TEXT,
                                       CRWcertCatalog TEXT,
                                       FacultyAdvisor TEXT,
                                       TAYN TEXT,
                                       LatestMilestoneFormSem TEXT,
                                       InternationalStudentYN TEXT,
                                       Language TEXT,
                                       LanguageDateFulfilled TEXT,
                                       LanguageReqWaivedBy TEXT,
                                       LanguageReqWaivedDate TEXT,
                                       ExamCommitteeFormDate TEXT,
                                       ExamCommChair TEXT,
                                       ExamCommCoChair TEXT,
                                       ExamComm2nd TEXT,
                                       ExamComm3rd TEXT,
                                       FirstSemRegFEP TEXT,
                                       ExamsCompleteDate TEXT,
                                       ExamResult TEXT,
                                       RegDissPropSem TEXT,
                                       ProposalApprovedDate TEXT,
                                       DissertationTitle TEXT,
                                       CommitteeFormOnFileYN TEXT,
                                       DissCommChair TEXT,
                                       DissCommCoChair TEXT,
                                       DissComm2nd TEXT,
                                       DissComm3rd TEXT,
                                       DissComm4th TEXT,
                                       AdditionalDissComm TEXT,
                                       GraduatedSemester TEXT,
                                       Inactive TEXT,
                                       Notes TEXT,
                                       MAProfessionalResearch TEXT,
                                       LanguageSeePhD TEXT,
                                       PortfolioProposalApprovedDate TEXT,
                                       CommitteeChair TEXT,
                                       CoChair TEXT,
                                       Comm2 TEXT,
                                       Comm3 TEXT,
                                       DefenseDate TEXT,
                                       Result TEXT,
                                       GraduatedSem TEXT,
                                       InactiveCheck TEXT,
                                       PersonalEmail TEXT,
                                       Address TEXT,
                                       Country TEXT,
                                       Employment TEXT,
                                       SocialMedia TEXT,
                                       AlumniNotes TEXT )''')
        conn.commit()
    conn.close()


def add_student(lastname, firstname, studentid, course, Program, Artschool, SubPlanText, FirstSemester, Catalog, HGHRcertCatalog, TranslCertCatalog, \
                CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
                , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate,ExamCommitteeFormDate, \
                ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
                ExamResult, RegDissPropSem, ProposalApprovedDate,DissertationTitle, CommitteeFormOnFileYN, \
                DissCommChair,DissCommCoChair,DissComm2nd,DissComm3rd,DissComm4th, AdditionalDissComm, GraduatedSemester, \
                Inactive,Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate,CommitteeChair, \
                CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address, Country, \
                Employment, SocialMedia, AlumniNotes):
    conn = sqlite3.connect('amohsen.db')
    c = conn.cursor()
    c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
     ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",\
              (lastname, firstname, studentid, course, Program, Artschool,SubPlanText, FirstSemester, Catalog, HGHRcertCatalog, TranslCertCatalog, \
                CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
                , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate,ExamCommitteeFormDate, \
                ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
                ExamResult, RegDissPropSem, ProposalApprovedDate,DissertationTitle, CommitteeFormOnFileYN, \
                DissCommChair,DissCommCoChair,DissComm2nd,DissComm3rd,DissComm4th, AdditionalDissComm, GraduatedSemester, \
                Inactive,Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate,CommitteeChair, \
                CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address, Country, \
                Employment, SocialMedia, AlumniNotes))
    conn.commit()
    conn.close()


def delete_student(studentid):
    conn = sqlite3.connect('amohsen.db')
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE StudentID=?", (studentid,))
    conn.commit()
    conn.close()
import sqlite3
import streamlit as st


def create_database():
    conn = sqlite3.connect('amohsen.db')
    c = conn.cursor()
    c.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='students'
    """)
    if not c.fetchone():
        c.execute('''CREATE TABLE students (
                                       LastName TEXT,
                                       FirstName TEXT,
                                       StudentID TEXT PRIMARY KEY,
                                       Course TEXT,
                                       Program TEXT,
                                       ArtSchool TEXT,
                                       SubPlanText TEXT,
                                       FirstSemester TEXT,
                                       Catalog TEXT,
                                       HGHRcertCatalog TEXT,
                                       TranslCertCatalog TEXT,
                                       CRWcertCatalog TEXT,
                                       FacultyAdvisor TEXT,
                                       TAYN TEXT,
                                       LatestMilestoneFormSem TEXT,
                                       InternationalStudentYN TEXT,
                                       Language TEXT,
                                       LanguageDateFulfilled TEXT,
                                       LanguageReqWaivedBy TEXT,
                                       LanguageReqWaivedDate TEXT,
                                       ExamCommitteeFormDate TEXT,
                                       ExamCommChair TEXT,
                                       ExamCommCoChair TEXT,
                                       ExamComm2nd TEXT,
                                       ExamComm3rd TEXT,
                                       FirstSemRegFEP TEXT,
                                       ExamsCompleteDate TEXT,
                                       ExamResult TEXT,
                                       RegDissPropSem TEXT,
                                       ProposalApprovedDate TEXT,
                                       DissertationTitle TEXT,
                                       CommitteeFormOnFileYN TEXT,
                                       DissCommChair TEXT,
                                       DissCommCoChair TEXT,
                                       DissComm2nd TEXT,
                                       DissComm3rd TEXT,
                                       DissComm4th TEXT,
                                       AdditionalDissComm TEXT,
                                       GraduatedSemester TEXT,
                                       Inactive TEXT,
                                       Notes TEXT,
                                       MAProfessionalResearch TEXT,
                                       LanguageSeePhD TEXT,
                                       PortfolioProposalApprovedDate TEXT,
                                       CommitteeChair TEXT,
                                       CoChair TEXT,
                                       Comm2 TEXT,
                                       Comm3 TEXT,
                                       DefenseDate TEXT,
                                       Result TEXT,
                                       GraduatedSem TEXT,
                                       InactiveCheck TEXT,
                                       PersonalEmail TEXT,
                                       Address TEXT,
                                       Country TEXT,
                                       Employment TEXT,
                                       SocialMedia TEXT,
                                       AlumniNotes TEXT )''')
        conn.commit()
    conn.close()


def add_student(lastname, firstname, studentid, course, Program, Artschool, SubPlanText, FirstSemester, Catalog, HGHRcertCatalog, TranslCertCatalog, \
                CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
                , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate,ExamCommitteeFormDate, \
                ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
                ExamResult, RegDissPropSem, ProposalApprovedDate,DissertationTitle, CommitteeFormOnFileYN, \
                DissCommChair,DissCommCoChair,DissComm2nd,DissComm3rd,DissComm4th, AdditionalDissComm, GraduatedSemester, \
                Inactive,Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate,CommitteeChair, \
                CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address, Country, \
                Employment, SocialMedia, AlumniNotes):
    conn = sqlite3.connect('amohsen.db')
    c = conn.cursor()
    c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
     ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",\
              (lastname, firstname, studentid, course, Program, Artschool,SubPlanText, FirstSemester, Catalog, HGHRcertCatalog, TranslCertCatalog, \
                CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
                , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate,ExamCommitteeFormDate, \
                ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
                ExamResult, RegDissPropSem, ProposalApprovedDate,DissertationTitle, CommitteeFormOnFileYN, \
                DissCommChair,DissCommCoChair,DissComm2nd,DissComm3rd,DissComm4th, AdditionalDissComm, GraduatedSemester, \
                Inactive,Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate,CommitteeChair, \
                CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address, Country, \
                Employment, SocialMedia, AlumniNotes))
    conn.commit()
    conn.close()


def delete_student(studentid):
    conn = sqlite3.connect('amohsen.db')
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE StudentID=?", (studentid,))
    conn.commit()
    conn.close()


def update_student(studentid,FirstName,LastName,Course, Program, ArtSchool, SubPlanText, FirstSemester, Catalog, HGHRcertCatalog, TranslCertCatalog, \
                    CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
                    , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate,ExamCommitteeFormDate, \
                    ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
                    ExamResult, RegDissPropSem, ProposalApprovedDate, DissertationTitle, CommitteeFormOnFileYN, \
                    DissCommChair, DissCommCoChair, DissComm2nd, DissComm3rd, DissComm4th, AdditionalDissComm,GraduatedSemester, \
                    Inactive, Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate,CommitteeChair, \
                    CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address,Country, \
                    Employment, SocialMedia, AlumniNotes
                    ):
    conn = sqlite3.connect('amohsen.db')
    c = conn.cursor()
    if FirstName is not None:
        c.execute("UPDATE students SET FirstName = ? WHERE StudentID = ?", (FirstName, studentid))
    if LastName is not None:
        c.execute("UPDATE students SET LastName = ? WHERE StudentID = ?", (LastName, studentid))
    if Course is not None:
        c.execute("UPDATE students SET Course = ? WHERE StudentID = ?", (Course, studentid))
    if Program is not None:
        c.execute("UPDATE students SET Program = ? WHERE StudentID = ?", (Program, studentid))
    if ArtSchool is not None:
        c.execute("UPDATE students SET ArtSchool = ? WHERE StudentID = ?", (ArtSchool, studentid))
    if SubPlanText is not None:
        c.execute("UPDATE students SET SubPlanText = ? WHERE StudentID = ?", (SubPlanText, studentid))
    if FirstSemester is not None:
        c.execute("UPDATE students SET FirstSemester = ? WHERE StudentID = ?", (FirstSemester, studentid))
    if Catalog is not None:
        c.execute("UPDATE students SET Catalog = ? WHERE StudentID = ?", (Catalog, studentid))
    if HGHRcertCatalog is not None:
        c.execute("UPDATE students SET HGHRcertCatalog = ? WHERE StudentID = ?", (HGHRcertCatalog, studentid))
    if TranslCertCatalog is not None:
        c.execute("UPDATE students SET TranslCertCatalog = ? WHERE StudentID = ?", (TranslCertCatalog, studentid))
    if CRWcertCatalog is not None:
        c.execute("UPDATE students SET CRWcertCatalog = ? WHERE StudentID = ?", (CRWcertCatalog, studentid))
    if FacultyAdvisor is not None:
        c.execute("UPDATE students SET FacultyAdvisor = ? WHERE StudentID = ?", (FacultyAdvisor, studentid))
    if TAYN is not None:
        c.execute("UPDATE students SET TAYN = ? WHERE StudentID = ?", (TAYN, studentid))
    if LatestMilestoneFormSem is not None:
        c.execute("UPDATE students SET LatestMilestoneFormSem = ? WHERE StudentID = ?", (LatestMilestoneFormSem, studentid))
    if InternationalStudentYN is not None:
        c.execute("UPDATE students SET InternationalStudentYN = ? WHERE StudentID = ?", (InternationalStudentYN, studentid))
    if Language is not None:
        c.execute("UPDATE students SET Language = ? WHERE StudentID = ?", (Language, studentid))
    if LanguageDateFulfilled is not None:
        c.execute("UPDATE students SET LanguageDateFulfilled = ? WHERE StudentID = ?", (LanguageDateFulfilled, studentid))
    if LanguageReqWaivedBy is not None:
        c.execute("UPDATE students SET LanguageReqWaivedBy = ? WHERE StudentID = ?", (LanguageReqWaivedBy, studentid))
    if LanguageReqWaivedDate is not None:
        c.execute("UPDATE students SET LanguageReqWaivedDate = ? WHERE StudentID = ?", (LanguageReqWaivedDate, studentid))
    if ExamCommitteeFormDate is not None:
        c.execute("UPDATE students SET ExamCommitteeFormDate = ? WHERE StudentID = ?", (ExamCommitteeFormDate, studentid))
    if ExamCommChair is not None:
        c.execute("UPDATE students SET ExamCommChair = ? WHERE StudentID = ?", (ExamCommChair, studentid))
    if ExamCommCoChair is not None:
        c.execute("UPDATE students SET ExamCommCoChair = ? WHERE StudentID = ?", (ExamCommCoChair, studentid))
    if ExamComm2nd is not None:
        c.execute("UPDATE students SET ExamComm2nd = ? WHERE StudentID = ?", (ExamComm2nd, studentid))
    if ExamComm3rd is not None:
        c.execute("UPDATE students SET ExamComm3rd = ? WHERE StudentID = ?", (ExamComm3rd, studentid))
    if FirstSemRegFEP is not None:
        c.execute("UPDATE students SET FirstSemRegFEP = ? WHERE StudentID = ?", (FirstSemRegFEP, studentid))
    if ExamsCompleteDate is not None:
        c.execute("UPDATE students SET ExamsCompleteDate = ? WHERE StudentID = ?", (ExamsCompleteDate, studentid))
    if ExamResult is not None:
        c.execute("UPDATE students SET ExamResult = ? WHERE StudentID = ?", (ExamResult, studentid))
    if RegDissPropSem is not None:
        c.execute("UPDATE students SET RegDissPropSem = ? WHERE StudentID = ?", (RegDissPropSem, studentid))
    if ProposalApprovedDate is not None:
        c.execute("UPDATE students SET ProposalApprovedDate = ? WHERE StudentID = ?", (ProposalApprovedDate, studentid))
    if DissertationTitle is not None:
        c.execute("UPDATE students SET DissertationTitle = ? WHERE StudentID = ?", (DissertationTitle, studentid))
    if CommitteeFormOnFileYN is not None:
        c.execute("UPDATE students SET CommitteeFormOnFileYN = ? WHERE StudentID = ?", (CommitteeFormOnFileYN, studentid))
    if DissCommChair is not None:
        c.execute("UPDATE students SET DissCommChair = ? WHERE StudentID = ?", (DissCommChair, studentid))
    if DissCommCoChair is not None:
        c.execute("UPDATE students SET DissCommCoChair = ? WHERE StudentID = ?", (DissCommCoChair, studentid))
    if DissComm2nd is not None:
        c.execute("UPDATE students SET DissComm2nd = ? WHERE StudentID = ?", (DissComm2nd, studentid))
    if DissComm3rd is not None:
        c.execute("UPDATE students SET DissComm3rd = ? WHERE StudentID = ?", (DissComm3rd, studentid))
    if DissComm4th is not None:
        c.execute("UPDATE students SET DissComm4th = ? WHERE StudentID = ?", (DissComm4th, studentid))
    if AdditionalDissComm is not None:
        c.execute("UPDATE students SET AdditionalDissComm = ? WHERE StudentID = ?", (AdditionalDissComm, studentid))
    if GraduatedSemester is not None:
        c.execute("UPDATE students SET GraduatedSemester = ? WHERE StudentID = ?", (GraduatedSemester, studentid))
    if Inactive is not None:
        c.execute("UPDATE students SET Inactive = ? WHERE StudentID = ?", (Inactive, studentid))
    if Notes is not None:
        c.execute("UPDATE students SET Notes = ? WHERE StudentID = ?", (Notes, studentid))
    if MAProfessionalResearch is not None:
        c.execute("UPDATE students SET MAProfessionalResearch = ? WHERE StudentID = ?", (MAProfessionalResearch, studentid))
    if LanguageSeePhD is not None:
        c.execute("UPDATE students SET LanguageSeePhD = ? WHERE StudentID = ?", (LanguageSeePhD, studentid))
    if PortfolioProposalApprovedDate is not None:
        c.execute("UPDATE students SET PortfolioProposalApprovedDate = ? WHERE StudentID = ?", (PortfolioProposalApprovedDate, studentid))
    if CommitteeChair is not None:
        c.execute("UPDATE students SET CommitteeChair = ? WHERE StudentID = ?", (CommitteeChair, studentid))
    if CoChair is not None:
        c.execute("UPDATE students SET CoChair = ? WHERE StudentID = ?", (CoChair, studentid))
    if Comm2 is not None:
        c.execute("UPDATE students SET Comm2 = ? WHERE StudentID = ?", (Comm2, studentid))
    if Comm3 is not None:
        c.execute("UPDATE students SET Comm3 = ? WHERE StudentID = ?", (Comm3, studentid))
    if DefenseDate is not None:
        c.execute("UPDATE students SET DefenseDate = ? WHERE StudentID = ?", (DefenseDate, studentid))
    if Result is not None:
        c.execute("UPDATE students SET Result = ? WHERE StudentID = ?", (Result, studentid))
    if GraduatedSem is not None:
        c.execute("UPDATE students SET GraduatedSem = ? WHERE StudentID = ?", (GraduatedSem, studentid))
    if InactiveCheck is not None:
        c.execute("UPDATE students SET InactiveCheck = ? WHERE StudentID = ?", (InactiveCheck, studentid))
    if PersonalEmail is not None:
        c.execute("UPDATE students SET PersonalEmail = ? WHERE StudentID = ?", (PersonalEmail, studentid))
    if Address is not None:
        c.execute("UPDATE students SET Address = ? WHERE StudentID = ?", (Address, studentid))
    if Country is not None:
        c.execute("UPDATE students SET Country = ? WHERE StudentID = ?", (Country, studentid))
    if Employment is not None:
        c.execute("UPDATE students SET Employment = ? WHERE StudentID = ?", (Employment, studentid))
    if SocialMedia is not None:
        c.execute("UPDATE students SET SocialMedia = ? WHERE StudentID = ?", (SocialMedia, studentid))
    if AlumniNotes is not None:
        c.execute("UPDATE students SET AlumniNotes = ? WHERE StudentID = ?", (AlumniNotes, studentid))
    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect('amohsen.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")

    # Fetch column names
    columns = [description[0] for description in c.description]

    # Fetch data
    students = c.fetchall()

    # Map column names to data
    students_with_columns = [dict(zip(columns, student)) for student in students]

    conn.close()
    return students_with_columns


def search_student(lastname, firstname, studentid, course, Program, Artschool, SubPlanText, FirstSemester, Catalog, HGHRcertCatalog, TranslCertCatalog, \
                CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
                , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate,ExamCommitteeFormDate, \
                ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
                ExamResult, RegDissPropSem, ProposalApprovedDate,DissertationTitle, CommitteeFormOnFileYN, \
                DissCommChair,DissCommCoChair,DissComm2nd,DissComm3rd,DissComm4th, AdditionalDissComm, GraduatedSemester, \
                Inactive,Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate,CommitteeChair, \
                CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address, Country, \
                Employment, SocialMedia, AlumniNotes):
    values_list = [
        "LastName",
        "FirstName",
        "StudentID",
        "Course",
        "Program",
        "Artschool",
        "SubPlanText",
        "FirstSemester",
        "Catalog",
        "HGHRcertCatalog",
        "TranslCertCatalog",
        "CRWcertCatalog",
        "FacultyAdvisor",
        "TAYN",
        "LatestMilestoneFormSem",
        "InternationalStudentYN",
        "Language",
        "LanguageDateFulfilled",
        "LanguageReqWaivedBy",
        "LanguageReqWaivedDate",
        "ExamCommitteeFormDate",
        "ExamCommChair",
        "ExamCommCoChair",
        "ExamComm2nd",
        "ExamComm3rd",
        "FirstSemRegFEP",
        "ExamsCompleteDate",
        "ExamResult",
        "RegDissPropSem",
        "ProposalApprovedDate",
        "DissertationTitle",
        "CommitteeFormOnFileYN",
        "DissCommChair",
        "DissCommCoChair",
        "DissComm2nd",
        "DissComm3rd",
        "DissComm4th",
        "AdditionalDissComm",
        "GraduatedSemester",
        "Inactive",
        "Notes",
        "MAProfessionalResearch",
        "LanguageSeePhD",
        "PortfolioProposalApprovedDate",
        "CommitteeChair",
        "CoChair",
        "Comm2",
        "Comm3",
        "DefenseDate",
        "Result",
        "GraduatedSem",
        "InactiveCheck",
        "PersonalEmail",
        "Address",
        "Country",
        "Employment",
        "SocialMedia",
        "AlumniNotes"
    ]
    par = [lastname, firstname, studentid, course, Program, Artschool, SubPlanText, FirstSemester, Catalog,
           HGHRcertCatalog, TranslCertCatalog, \
           CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
        , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate, ExamCommitteeFormDate, \
           ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
           ExamResult, RegDissPropSem, ProposalApprovedDate, DissertationTitle, CommitteeFormOnFileYN, \
           DissCommChair, DissCommCoChair, DissComm2nd, DissComm3rd, DissComm4th, AdditionalDissComm, GraduatedSemester, \
           Inactive, Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate, CommitteeChair, \
           CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address, Country, \
           Employment, SocialMedia, AlumniNotes]

    conn = sqlite3.connect('amohsen.db')
    c = conn.cursor()
    conditions = []
    base_query = "SELECT * FROM students WHERE"
    par = [lastname, firstname, studentid, course, Program, Artschool, SubPlanText, FirstSemester, Catalog,
           HGHRcertCatalog, TranslCertCatalog, \
           CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
        , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate, ExamCommitteeFormDate, \
           ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
           ExamResult, RegDissPropSem, ProposalApprovedDate, DissertationTitle, CommitteeFormOnFileYN, \
           DissCommChair, DissCommCoChair, DissComm2nd, DissComm3rd, DissComm4th, AdditionalDissComm, GraduatedSemester, \
           Inactive, Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate, CommitteeChair, \
           CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address, Country, \
           Employment, SocialMedia, AlumniNotes]
    # for column, value in parameters.items():
    #     if value is not None:
    #         conditions.append(f"{value} = ?")
    for column, value in zip(values_list, par):
        if value is not None and value != "":
            conditions.append(f"{column} = ?")

    # Combine conditions with AND and append to the base query
    if conditions:
        full_query = f"{base_query} {' AND '.join(conditions)}"
    else:
        # If no conditions are added, select all records
        full_query = f"{base_query} 1"

    # Execute the query with the provided parameters


    c.execute(full_query, tuple(filter(None,par)))
    columns = [description[0] for description in c.description]

    # Fetch data
    students = c.fetchall()

    # Map column names to data
    students_with_columns = [dict(zip(columns, student)) for student in students]

    conn.close()
    return students_with_columns

def update_student(studentid,FirstName,LastName,Course, Program, ArtSchool, SubPlanText, FirstSemester, Catalog, HGHRcertCatalog, TranslCertCatalog, \
                    CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
                    , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate,ExamCommitteeFormDate, \
                    ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
                    ExamResult, RegDissPropSem, ProposalApprovedDate, DissertationTitle, CommitteeFormOnFileYN, \
                    DissCommChair, DissCommCoChair, DissComm2nd, DissComm3rd, DissComm4th, AdditionalDissComm,GraduatedSemester, \
                    Inactive, Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate,CommitteeChair, \
                    CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address,Country, \
                    Employment, SocialMedia, AlumniNotes
                    ):
    conn = sqlite3.connect('amohsen.db')
    c = conn.cursor()
    if FirstName is not None:
        c.execute("UPDATE students SET FirstName = ? WHERE StudentID = ?", (FirstName, studentid))
    if LastName is not None:
        c.execute("UPDATE students SET LastName = ? WHERE StudentID = ?", (LastName, studentid))
    if Course is not None:
        c.execute("UPDATE students SET Course = ? WHERE StudentID = ?", (Course, studentid))
    if Program is not None:
        c.execute("UPDATE students SET Program = ? WHERE StudentID = ?", (Program, studentid))
    if ArtSchool is not None:
        c.execute("UPDATE students SET ArtSchool = ? WHERE StudentID = ?", (ArtSchool, studentid))
    if SubPlanText is not None:
        c.execute("UPDATE students SET SubPlanText = ? WHERE StudentID = ?", (SubPlanText, studentid))
    if FirstSemester is not None:
        c.execute("UPDATE students SET FirstSemester = ? WHERE StudentID = ?", (FirstSemester, studentid))
    if Catalog is not None:
        c.execute("UPDATE students SET Catalog = ? WHERE StudentID = ?", (Catalog, studentid))
    if HGHRcertCatalog is not None:
        c.execute("UPDATE students SET HGHRcertCatalog = ? WHERE StudentID = ?", (HGHRcertCatalog, studentid))
    if TranslCertCatalog is not None:
        c.execute("UPDATE students SET TranslCertCatalog = ? WHERE StudentID = ?", (TranslCertCatalog, studentid))
    if CRWcertCatalog is not None:
        c.execute("UPDATE students SET CRWcertCatalog = ? WHERE StudentID = ?", (CRWcertCatalog, studentid))
    if FacultyAdvisor is not None:
        c.execute("UPDATE students SET FacultyAdvisor = ? WHERE StudentID = ?", (FacultyAdvisor, studentid))
    if TAYN is not None:
        c.execute("UPDATE students SET TAYN = ? WHERE StudentID = ?", (TAYN, studentid))
    if LatestMilestoneFormSem is not None:
        c.execute("UPDATE students SET LatestMilestoneFormSem = ? WHERE StudentID = ?", (LatestMilestoneFormSem, studentid))
    if InternationalStudentYN is not None:
        c.execute("UPDATE students SET InternationalStudentYN = ? WHERE StudentID = ?", (InternationalStudentYN, studentid))
    if Language is not None:
        c.execute("UPDATE students SET Language = ? WHERE StudentID = ?", (Language, studentid))
    if LanguageDateFulfilled is not None:
        c.execute("UPDATE students SET LanguageDateFulfilled = ? WHERE StudentID = ?", (LanguageDateFulfilled, studentid))
    if LanguageReqWaivedBy is not None:
        c.execute("UPDATE students SET LanguageReqWaivedBy = ? WHERE StudentID = ?", (LanguageReqWaivedBy, studentid))
    if LanguageReqWaivedDate is not None:
        c.execute("UPDATE students SET LanguageReqWaivedDate = ? WHERE StudentID = ?", (LanguageReqWaivedDate, studentid))
    if ExamCommitteeFormDate is not None:
        c.execute("UPDATE students SET ExamCommitteeFormDate = ? WHERE StudentID = ?", (ExamCommitteeFormDate, studentid))
    if ExamCommChair is not None:
        c.execute("UPDATE students SET ExamCommChair = ? WHERE StudentID = ?", (ExamCommChair, studentid))
    if ExamCommCoChair is not None:
        c.execute("UPDATE students SET ExamCommCoChair = ? WHERE StudentID = ?", (ExamCommCoChair, studentid))
    if ExamComm2nd is not None:
        c.execute("UPDATE students SET ExamComm2nd = ? WHERE StudentID = ?", (ExamComm2nd, studentid))
    if ExamComm3rd is not None:
        c.execute("UPDATE students SET ExamComm3rd = ? WHERE StudentID = ?", (ExamComm3rd, studentid))
    if FirstSemRegFEP is not None:
        c.execute("UPDATE students SET FirstSemRegFEP = ? WHERE StudentID = ?", (FirstSemRegFEP, studentid))
    if ExamsCompleteDate is not None:
        c.execute("UPDATE students SET ExamsCompleteDate = ? WHERE StudentID = ?", (ExamsCompleteDate, studentid))
    if ExamResult is not None:
        c.execute("UPDATE students SET ExamResult = ? WHERE StudentID = ?", (ExamResult, studentid))
    if RegDissPropSem is not None:
        c.execute("UPDATE students SET RegDissPropSem = ? WHERE StudentID = ?", (RegDissPropSem, studentid))
    if ProposalApprovedDate is not None:
        c.execute("UPDATE students SET ProposalApprovedDate = ? WHERE StudentID = ?", (ProposalApprovedDate, studentid))
    if DissertationTitle is not None:
        c.execute("UPDATE students SET DissertationTitle = ? WHERE StudentID = ?", (DissertationTitle, studentid))
    if CommitteeFormOnFileYN is not None:
        c.execute("UPDATE students SET CommitteeFormOnFileYN = ? WHERE StudentID = ?", (CommitteeFormOnFileYN, studentid))
    if DissCommChair is not None:
        c.execute("UPDATE students SET DissCommChair = ? WHERE StudentID = ?", (DissCommChair, studentid))
    if DissCommCoChair is not None:
        c.execute("UPDATE students SET DissCommCoChair = ? WHERE StudentID = ?", (DissCommCoChair, studentid))
    if DissComm2nd is not None:
        c.execute("UPDATE students SET DissComm2nd = ? WHERE StudentID = ?", (DissComm2nd, studentid))
    if DissComm3rd is not None:
        c.execute("UPDATE students SET DissComm3rd = ? WHERE StudentID = ?", (DissComm3rd, studentid))
    if DissComm4th is not None:
        c.execute("UPDATE students SET DissComm4th = ? WHERE StudentID = ?", (DissComm4th, studentid))
    if AdditionalDissComm is not None:
        c.execute("UPDATE students SET AdditionalDissComm = ? WHERE StudentID = ?", (AdditionalDissComm, studentid))
    if GraduatedSemester is not None:
        c.execute("UPDATE students SET GraduatedSemester = ? WHERE StudentID = ?", (GraduatedSemester, studentid))
    if Inactive is not None:
        c.execute("UPDATE students SET Inactive = ? WHERE StudentID = ?", (Inactive, studentid))
    if Notes is not None:
        c.execute("UPDATE students SET Notes = ? WHERE StudentID = ?", (Notes, studentid))
    if MAProfessionalResearch is not None:
        c.execute("UPDATE students SET MAProfessionalResearch = ? WHERE StudentID = ?", (MAProfessionalResearch, studentid))
    if LanguageSeePhD is not None:
        c.execute("UPDATE students SET LanguageSeePhD = ? WHERE StudentID = ?", (LanguageSeePhD, studentid))
    if PortfolioProposalApprovedDate is not None:
        c.execute("UPDATE students SET PortfolioProposalApprovedDate = ? WHERE StudentID = ?", (PortfolioProposalApprovedDate, studentid))
    if CommitteeChair is not None:
        c.execute("UPDATE students SET CommitteeChair = ? WHERE StudentID = ?", (CommitteeChair, studentid))
    if CoChair is not None:
        c.execute("UPDATE students SET CoChair = ? WHERE StudentID = ?", (CoChair, studentid))
    if Comm2 is not None:
        c.execute("UPDATE students SET Comm2 = ? WHERE StudentID = ?", (Comm2, studentid))
    if Comm3 is not None:
        c.execute("UPDATE students SET Comm3 = ? WHERE StudentID = ?", (Comm3, studentid))
    if DefenseDate is not None:
        c.execute("UPDATE students SET DefenseDate = ? WHERE StudentID = ?", (DefenseDate, studentid))
    if Result is not None:
        c.execute("UPDATE students SET Result = ? WHERE StudentID = ?", (Result, studentid))
    if GraduatedSem is not None:
        c.execute("UPDATE students SET GraduatedSem = ? WHERE StudentID = ?", (GraduatedSem, studentid))
    if InactiveCheck is not None:
        c.execute("UPDATE students SET InactiveCheck = ? WHERE StudentID = ?", (InactiveCheck, studentid))
    if PersonalEmail is not None:
        c.execute("UPDATE students SET PersonalEmail = ? WHERE StudentID = ?", (PersonalEmail, studentid))
    if Address is not None:
        c.execute("UPDATE students SET Address = ? WHERE StudentID = ?", (Address, studentid))
    if Country is not None:
        c.execute("UPDATE students SET Country = ? WHERE StudentID = ?", (Country, studentid))
    if Employment is not None:
        c.execute("UPDATE students SET Employment = ? WHERE StudentID = ?", (Employment, studentid))
    if SocialMedia is not None:
        c.execute("UPDATE students SET SocialMedia = ? WHERE StudentID = ?", (SocialMedia, studentid))
    if AlumniNotes is not None:
        c.execute("UPDATE students SET AlumniNotes = ? WHERE StudentID = ?", (AlumniNotes, studentid))
    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect('amohsen.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")

    # Fetch column names
    columns = [description[0] for description in c.description]

    # Fetch data
    students = c.fetchall()

    # Map column names to data
    students_with_columns = [dict(zip(columns, student)) for student in students]

    conn.close()
    return students_with_columns


def search_student(lastname, firstname, studentid, course, Program, Artschool, SubPlanText, FirstSemester, Catalog, HGHRcertCatalog, TranslCertCatalog, \
                CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
                , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate,ExamCommitteeFormDate, \
                ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
                ExamResult, RegDissPropSem, ProposalApprovedDate,DissertationTitle, CommitteeFormOnFileYN, \
                DissCommChair,DissCommCoChair,DissComm2nd,DissComm3rd,DissComm4th, AdditionalDissComm, GraduatedSemester, \
                Inactive,Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate,CommitteeChair, \
                CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address, Country, \
                Employment, SocialMedia, AlumniNotes):
    values_list = [
        "LastName",
        "FirstName",
        "StudentID",
        "Course",
        "Program",
        "Artschool",
        "SubPlanText",
        "FirstSemester",
        "Catalog",
        "HGHRcertCatalog",
        "TranslCertCatalog",
        "CRWcertCatalog",
        "FacultyAdvisor",
        "TAYN",
        "LatestMilestoneFormSem",
        "InternationalStudentYN",
        "Language",
        "LanguageDateFulfilled",
        "LanguageReqWaivedBy",
        "LanguageReqWaivedDate",
        "ExamCommitteeFormDate",
        "ExamCommChair",
        "ExamCommCoChair",
        "ExamComm2nd",
        "ExamComm3rd",
        "FirstSemRegFEP",
        "ExamsCompleteDate",
        "ExamResult",
        "RegDissPropSem",
        "ProposalApprovedDate",
        "DissertationTitle",
        "CommitteeFormOnFileYN",
        "DissCommChair",
        "DissCommCoChair",
        "DissComm2nd",
        "DissComm3rd",
        "DissComm4th",
        "AdditionalDissComm",
        "GraduatedSemester",
        "Inactive",
        "Notes",
        "MAProfessionalResearch",
        "LanguageSeePhD",
        "PortfolioProposalApprovedDate",
        "CommitteeChair",
        "CoChair",
        "Comm2",
        "Comm3",
        "DefenseDate",
        "Result",
        "GraduatedSem",
        "InactiveCheck",
        "PersonalEmail",
        "Address",
        "Country",
        "Employment",
        "SocialMedia",
        "AlumniNotes"
    ]
    par = [lastname, firstname, studentid, course, Program, Artschool, SubPlanText, FirstSemester, Catalog,
           HGHRcertCatalog, TranslCertCatalog, \
           CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
        , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate, ExamCommitteeFormDate, \
           ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
           ExamResult, RegDissPropSem, ProposalApprovedDate, DissertationTitle, CommitteeFormOnFileYN, \
           DissCommChair, DissCommCoChair, DissComm2nd, DissComm3rd, DissComm4th, AdditionalDissComm, GraduatedSemester, \
           Inactive, Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate, CommitteeChair, \
           CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address, Country, \
           Employment, SocialMedia, AlumniNotes]

    conn = sqlite3.connect('amohsen.db')
    c = conn.cursor()
    conditions = []
    base_query = "SELECT * FROM students WHERE"
    par = [lastname, firstname, studentid, course, Program, Artschool, SubPlanText, FirstSemester, Catalog,
           HGHRcertCatalog, TranslCertCatalog, \
           CRWcertCatalog, FacultyAdvisor, TAYN, LatestMilestoneFormSem, InternationalStudentYN \
        , Language, LanguageDateFulfilled, LanguageReqWaivedBy, LanguageReqWaivedDate, ExamCommitteeFormDate, \
           ExamCommChair, ExamCommCoChair, ExamComm2nd, ExamComm3rd, FirstSemRegFEP, ExamsCompleteDate, \
           ExamResult, RegDissPropSem, ProposalApprovedDate, DissertationTitle, CommitteeFormOnFileYN, \
           DissCommChair, DissCommCoChair, DissComm2nd, DissComm3rd, DissComm4th, AdditionalDissComm, GraduatedSemester, \
           Inactive, Notes, MAProfessionalResearch, LanguageSeePhD, PortfolioProposalApprovedDate, CommitteeChair, \
           CoChair, Comm2, Comm3, DefenseDate, Result, GraduatedSem, InactiveCheck, PersonalEmail, Address, Country, \
           Employment, SocialMedia, AlumniNotes]
    # for column, value in parameters.items():
    #     if value is not None:
    #         conditions.append(f"{value} = ?")
    for column, value in zip(values_list, par):
        if value is not None and value != "":
            conditions.append(f"{column} = ?")

    # Combine conditions with AND and append to the base query
    if conditions:
        full_query = f"{base_query} {' AND '.join(conditions)}"
    else:
        # If no conditions are added, select all records
        full_query = f"{base_query} 1"

    # Execute the query with the provided parameters


    c.execute(full_query, tuple(filter(None,par)))
    columns = [description[0] for description in c.description]

    # Fetch data
    students = c.fetchall()

    # Map column names to data
    students_with_columns = [dict(zip(columns, student)) for student in students]

    conn.close()
    return students_with_columns