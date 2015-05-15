#include "ReadTwiss.h"

void ReadTwiss(string in, vector<string> *K, vector<string> *N, 
	       vector<string> *Pa, vector<string> *Kn, vector<string> *Nn, 
	       vector<string> *Pan, vector<double> *P, vector<double> *L, 
	       vector<double> *A1, vector<double> *A2, vector<double> *A3, 
	       vector<double> *A4)

{

  cout<<"Start ReadTwiss"<<endl;

  K->clear();
  N->clear();
  Pa->clear();
  P->clear();
  L->clear();
  A1->clear();
  A2->clear();
  A3->clear();
  A4->clear();
  
  string tKs, tNs, tTs;
  double tPs, tLs, tA1s, tA2s, tA3s, tA4s;
  string str_tmp;
  char chr_tmp[256];

  ifstream InputFile( in.c_str() );
  if ( !InputFile ){
    cout<<"Impossible to open the file \""<<in<<"\"!!"<<endl;
    exit(0);
  } else {
    // Disregard the header
    while ( InputFile.getline(chr_tmp, 256) ) {
      str_tmp = chr_tmp;
      if (str_tmp.find("KEYWORD",0) != string::npos) {
	InputFile.getline(chr_tmp, 256);
	break;
      }
    }
    // Start filling up the vectors
    while ( 1 ) {
      InputFile>>tKs>>tNs>>tTs>>tPs>>tLs>>tA1s>>tA2s>>tA3s>>tA4s;
      if (!InputFile.good())
	break;
      K  -> push_back(tKs);
      N  -> push_back(tNs);
      Pa -> push_back(tTs);
      P  -> push_back(tPs);
      L  -> push_back(tLs);
      A1 -> push_back(tA1s);
      A2 -> push_back(tA2s);
      A3 -> push_back(tA3s);
      A4 -> push_back(tA4s);
      // 
      // Element names without quotes
      Kn  -> push_back( tKs.substr(1, tKs.size()-2) );
      Nn  -> push_back( tNs.substr(1, tNs.size()-2) );
      Pan -> push_back( tTs.substr(1, tTs.size()-2) );
    }
    InputFile.close();
    //
    cout<<endl;
    cout<<"Reading from \""<<in<<"\""<<endl;
    cout<<"Total number of read elements: "<<K->size()<<endl;
    cout<<endl;
  }

  cout<<"End ReadTwiss"<<endl;

}

void ReadTwissNoDrifts(string in, vector<string> *K, vector<string> *N, 
		       vector<string> *Pa, vector<string> *Kn, vector<string> *Nn, 
		       vector<string> *Pan, vector<double> *P, vector<double> *L, 
		       vector<double> *A1, vector<double> *A2, vector<double> *A3, 
		       vector<double> *A4)

{

  K->clear();
  N->clear();
  Pa->clear();
  P->clear();
  L->clear();
  A1->clear();
  A2->clear();
  A3->clear();
  A4->clear();
  
  string tKs, tNs, tTs;
  double tPs, tLs, tA1s, tA2s, tA3s, tA4s;
  string str_tmp;
  char chr_tmp[256];

  ifstream InputFile( in.c_str() );
  if ( !InputFile ){
    cout<<"Impossible to open the file \""<<in<<"\"!!"<<endl;
    exit(0);
  } else {
    // Disregard the header
    while ( InputFile.getline(chr_tmp, 256) ) {
      str_tmp = chr_tmp;
      if (str_tmp.find("KEYWORD",0) != string::npos) {
	InputFile.getline(chr_tmp, 256);
	break;
      }
    }
    // Start filling up the vectors
    while ( 1 ) {
      InputFile>>tKs>>tNs>>tTs>>tPs>>tLs>>tA1s>>tA2s>>tA3s>>tA4s;
      if (!InputFile.good())
	break;
      if ( tKs.find("DRIFT",0) == string::npos ){
	K  -> push_back(tKs);
	N  -> push_back(tNs);
	Pa -> push_back(tTs);
	P  -> push_back(tPs);
	L  -> push_back(tLs);
	A1 -> push_back(tA1s);
	A2 -> push_back(tA2s);
	A3 -> push_back(tA3s);
	A4 -> push_back(tA4s);
	// Element names without quotes
	Kn  -> push_back( tKs.substr(1, tKs.size()-2) );
	Nn  -> push_back( tNs.substr(1, tNs.size()-2) );
	Pan -> push_back( tTs.substr(1, tTs.size()-2) );
      } 
    }
    InputFile.close();
    //
    cout<<endl;
    cout<<"Reading from \""<<in<<"\""<<endl;
    cout<<"Total number of read elements: "<<K->size()<<endl;
    cout<<endl;
  }

}


void ReadTwissK(string in, vector<string> *K, vector<string> *N, 
		vector<string> *Pa, vector<string> *Kn, vector<string> *Nn, 
		vector<string> *Pan, vector<double> *P, vector<double> *L, 
		vector<double> *KL, vector<double> *A1, vector<double> *A2, 
		vector<double> *A3, vector<double> *A4)
{
  K->clear();
  N->clear();
  Pa->clear();
  P->clear();
  L->clear();
  KL->clear();
  A1->clear();
  A2->clear();
  A3->clear();
  A4->clear();

  string tKs, tNs, tTs;
  double tPs, tLs, tKLs, tA1s, tA2s, tA3s, tA4s;
  string str_tmp;
  char chr_tmp[256];

  ifstream InputFile( in.c_str() );
  if ( !InputFile ){
    cout<<"Impossible to open the file \""<<in<<"\"!!"<<endl;
    exit(0);
  } else {
    // Disregard the header
    while ( InputFile.getline(chr_tmp, 256) ) {
      str_tmp = chr_tmp;
      if (str_tmp.find("KEYWORD",0) != string::npos) {
	InputFile.getline(chr_tmp, 256);
	break;
      }
    }
    // Start filling up the vectors
    while ( 1 ) {
      InputFile>>tKs>>tNs>>tTs>>tPs>>tLs>>tKLs>>tA1s>>tA2s>>tA3s>>tA4s;
      if (!InputFile.good())
	break;
      K  -> push_back(tKs);
      N  -> push_back(tNs);
      Pa -> push_back(tTs);
      P  -> push_back(tPs);
      L  -> push_back(tLs);
      KL -> push_back(tKLs);
      A1 -> push_back(tA1s);
      A2 -> push_back(tA2s);
      A3 -> push_back(tA3s);
      A4 -> push_back(tA4s);
      // 
      // Element names without quotes
      Kn  -> push_back( tKs.substr(1, tKs.size()-2) );
      Nn  -> push_back( tNs.substr(1, tNs.size()-2) );
      Pan -> push_back( tTs.substr(1, tTs.size()-2) );
    }
    InputFile.close();
    //
    cout<<endl;
    cout<<"Reading from \""<<in<<"\""<<endl;
    cout<<"Total number of read elements: "<<K->size()<<endl;
    cout<<endl;
  }

}

void ReadTwissDX(string in, vector<string> *K, vector<string> *N, vector<string> *Pa, 
		 vector<string> *Kn, vector<string> *Nn, vector<string> *Pan, 
		 vector<double> *P, vector<double> *L, vector<double> *A1, 
		 vector<double> *A2, vector<double> *A3, vector<double> *A4, 
		 vector<double> *DX, vector<double> *DY)
{
  K->clear();
  N->clear();
  Pa->clear();
  P->clear();
  L->clear();
  A1->clear();
  A2->clear();
  A3->clear();
  A4->clear();
  DX->clear();
  DY->clear();

  string tKs, tNs, tTs;
  double tPs, tLs, tA1s, tA2s, tA3s, tA4s, tDXs, tDYs;
  string str_tmp;
  char chr_tmp[256];

  ifstream InputFile( in.c_str() );
  if ( !InputFile ){
    cout<<"Impossible to open the file \""<<in<<"\"!!"<<endl;
    exit(0);
  } else {
    // Disregard the header
    while ( InputFile.getline(chr_tmp, 256) ) {
      str_tmp = chr_tmp;
      if (str_tmp.find("KEYWORD",0) != string::npos) {
	InputFile.getline(chr_tmp, 256);
	break;
      }
    }
    // Start filling up the vectors
    while ( 1 ) {
      InputFile>>tKs>>tNs>>tTs>>tPs>>tLs>>tA1s>>tA2s>>tA3s>>tA4s>>tDXs>>tDYs;
      if (!InputFile.good())
	break;
      K  -> push_back(tKs);
      N  -> push_back(tNs);
      Pa -> push_back(tTs);
      P  -> push_back(tPs);
      L  -> push_back(tLs);
      A1 -> push_back(tA1s);
      A2 -> push_back(tA2s);
      A3 -> push_back(tA3s);
      A4 -> push_back(tA4s);
      DX -> push_back(tDXs);
      DY -> push_back(tDYs);
      // Element names without quotes
      Kn  -> push_back( tKs.substr(1, tKs.size()-2) );
      Nn  -> push_back( tNs.substr(1, tNs.size()-2) );
      Pan -> push_back( tTs.substr(1, tTs.size()-2) );
    }
    InputFile.close();
    //
    cout<<endl;
    cout<<"Reading from \""<<in<<"\""<<endl;
    cout<<"Total number of read elements: "<<K->size()<<endl;
    cout<<endl;
  }

}

void ReadTwissDXNoDrifts(string in, vector<string> *K, vector<string> *N, vector<string> *Pa, 
			 vector<string> *Kn, vector<string> *Nn, vector<string> *Pan, 
			 vector<double> *P, vector<double> *L, vector<double> *A1, 
			 vector<double> *A2, vector<double> *A3, vector<double> *A4, 
			 vector<double> *DX, vector<double> *DY)
{
  K->clear();
  N->clear();
  Pa->clear();
  P->clear();
  L->clear();
  A1->clear();
  A2->clear();
  A3->clear();
  A4->clear();
  DX->clear();
  DY->clear();

  string tKs, tNs, tTs;
  double tPs, tLs, tA1s, tA2s, tA3s, tA4s, tDXs, tDYs;
  string str_tmp;
  char chr_tmp[256];

  ifstream InputFile( in.c_str() );
  if ( !InputFile ){
    cout<<"Impossible to open the file \""<<in<<"\"!!"<<endl;
    exit(0);
  } else {
    // Disregard the header
    while ( InputFile.getline(chr_tmp, 256) ) {
      str_tmp = chr_tmp;
      if (str_tmp.find("KEYWORD",0) != string::npos) {
	InputFile.getline(chr_tmp, 256);
	break;
      }
    }
    // Start filling up the vectors
    while ( 1 ) {
      InputFile>>tKs>>tNs>>tTs>>tPs>>tLs>>tA1s>>tA2s>>tA3s>>tA4s>>tDXs>>tDYs;
      if (!InputFile.good())
	break;
      if ( tKs.find("DRIFT",0) == string::npos ){
	K  -> push_back(tKs);
	N  -> push_back(tNs);
	Pa -> push_back(tTs);
	P  -> push_back(tPs);
	L  -> push_back(tLs);
	A1 -> push_back(tA1s);
	A2 -> push_back(tA2s);
	A3 -> push_back(tA3s);
	A4 -> push_back(tA4s);
	DX -> push_back(tDXs);
	DY -> push_back(tDYs);
	// Element names without quotes
	Kn  -> push_back( tKs.substr(1, tKs.size()-2) );
	Nn  -> push_back( tNs.substr(1, tNs.size()-2) );
	Pan -> push_back( tTs.substr(1, tTs.size()-2) );
      }
    }
    InputFile.close();
    //
    cout<<endl;
    cout<<"Reading from \""<<in<<"\""<<endl;
    cout<<"Total number of read elements: "<<K->size()<<endl;
    cout<<endl;
  }

}
